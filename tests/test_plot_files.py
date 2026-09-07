"""Offline file-boundary tests; these do not validate numerical calibration."""

import ast
import contextlib
import importlib.util
import io
import optparse
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

SCRIPTS = Path(__file__).resolve().parents[1] / "GuppyScreen/scripts"


def source_function(filename, name, namespace):
    """Run the actual function with numerical/plot dependencies substituted."""
    path = SCRIPTS / filename
    tree = ast.parse(path.read_text())
    node = next(
        n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name
    )
    module = ast.Module(body=[node], type_ignores=[])
    exec(compile(module, str(path), "exec"), namespace)
    return namespace[name]


def output_helper():
    path = SCRIPTS / "plot_output.py"
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location("plot_output_fixture", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.save_figure


class PlotFileTests(unittest.TestCase):
    def test_raw_logs_with_and_without_comment_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "raw.csv"
            expected = object()
            loader = types.SimpleNamespace(loadtxt=lambda *a, **k: expected)
            for filename in ("graph_belts.py", "calibrate_shaper.py"):
                parse = source_function(filename, "parse_log", {"np": loader})
                for prefix in ("", "#time,x,y,z\n"):
                    with self.subTest(filename=filename, prefix=prefix):
                        path.write_text(prefix + "0,1,2,3\n1,2,3,4\n")
                        self.assertIs(parse(str(path)), expected)

    def test_empty_logs_fail_clearly(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "empty.csv"
            for filename in ("graph_belts.py", "calibrate_shaper.py"):
                parse = source_function(
                    filename,
                    "parse_log",
                    {"np": types.SimpleNamespace(loadtxt=lambda *a, **k: [])},
                )
                for contents in ("", "# comment\n"):
                    with self.subTest(filename=filename, contents=contents):
                        path.write_text(contents)
                        with self.assertRaisesRegex(ValueError, "empty"):
                            parse(str(path))

    def test_plot_commands_preserve_existing_output_on_failed_save(self):
        self.check_output(fail=True)

    def test_plot_commands_replace_output_on_success(self):
        self.check_output(fail=False)

    def test_default_output_extension(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "plot"
            fig = types.SimpleNamespace(
                savefig=lambda path: Path(path).write_bytes(b"svg")
            )
            actual = output_helper()(fig, target, default_format="svg")
            self.assertEqual(actual, target.with_suffix(".svg"))
            self.assertEqual(actual.read_bytes(), b"svg")
            self.assertFalse(target.exists())

    def test_failed_promotion_preserves_previous_file_and_cleans_stage(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "plot.png"
            target.write_bytes(b"previous")
            fig = types.SimpleNamespace(
                savefig=lambda path: Path(path).write_bytes(b"new")
            )
            with patch.object(
                Path, "replace", side_effect=OSError("fixture promotion failure")
            ):
                with self.assertRaisesRegex(OSError, "fixture promotion failure"):
                    output_helper()(fig, target)
            self.assertEqual(target.read_bytes(), b"previous")
            self.assertEqual(list(Path(tmp).iterdir()), [target])

    def test_offline_belts_do_not_inspect_process_descriptors(self):
        opened = Mock(side_effect=AssertionError("must not inspect processes"))
        self.check_capture_wait(opened, offline=True)
        opened.assert_not_called()

    def test_live_belts_still_wait_for_open_captures(self):
        opened = Mock(side_effect=[True, False, False])
        sleep = self.check_capture_wait(opened, offline=False)
        self.assertEqual(opened.call_count, 3)
        sleep.assert_called_once_with(2)

    def check_capture_wait(self, opened, offline):
        sleep = Mock()
        parse = Mock(side_effect=ValueError("fixture reached parsing"))
        calibrate = source_function(
            "graph_belts.py",
            "belts_calibration",
            {
                "is_file_open": opened,
                "time": types.SimpleNamespace(sleep=sleep),
                "parse_log": parse,
            },
        )
        with self.assertRaisesRegex(ValueError, "fixture reached parsing"):
            calibrate(["a.csv", "b.csv"], **({"offline": True} if offline else {}))
        parse.assert_called_once_with("a.csv")
        return sleep

    def check_output(self, fail):
        for filename in ("graph_belts.py", "calibrate_shaper.py"):
            with self.subTest(filename=filename), tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp) / "plot.png"
                target.write_bytes(b"previous plot")

                class Figure:
                    def set_size_inches(self, *args):
                        pass

                    def savefig(self, path, **kwargs):
                        Path(path).write_bytes(b"replacement plot")
                        if fail:
                            raise OSError("fixture render failure")

                fig = Figure()
                namespace = {
                    "optparse": optparse,
                    "matplotlib": types.SimpleNamespace(
                        rcParams={"savefig.format": "png"}
                    ),
                    "pathlib": __import__("pathlib"),
                    "json": __import__("json"),
                    "belts_calibration": lambda *args: fig,
                    "parse_log": lambda *args: object(),
                    "calibrate_shaper": lambda *args: ("zv", [], None, {}),
                    "setup_matplotlib": lambda *args: None,
                    "plot_freq_response": lambda *args: fig,
                    "save_figure": output_helper(),
                }
                main = source_function(filename, "main", namespace)
                with patch.object(
                    sys, "argv", [filename, "-o", str(target), "a.csv", "b.csv"]
                ):
                    with contextlib.redirect_stdout(io.StringIO()):
                        if fail:
                            with self.assertRaisesRegex(
                                OSError, "fixture render failure"
                            ):
                                main()
                        else:
                            main()
                self.assertEqual(
                    target.read_bytes(),
                    b"previous plot" if fail else b"replacement plot",
                )
                self.assertEqual(list(Path(tmp).iterdir()), [target])


if __name__ == "__main__":
    unittest.main()
