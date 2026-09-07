"""Synthetic offline CLI acceptance; no resonance acquisition or printer connection."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

SCRIPTS = Path(__file__).resolve().parents[1] / "GuppyScreen/scripts"


class PlotNumericalTests(unittest.TestCase):
    def test_synthetic_logs_render_at_supported_frequency_limits(self):
        with tempfile.TemporaryDirectory(prefix="guppy-numerical-") as tmp:
            root = Path(tmp)
            t = np.arange(4096) / 512
            rng = np.random.default_rng(11)
            logs = []
            for name, shift in (("a", 0), ("b", 0.6)):
                data = np.column_stack(
                    [
                        t,
                        np.sin(2 * np.pi * (40 + shift) * t)
                        + 0.25 * np.sin(2 * np.pi * 80 * t),
                        0.8 * np.sin(2 * np.pi * (43 + shift) * t),
                        0.3 * np.sin(2 * np.pi * 65 * t),
                    ]
                )
                data[:, 1:] += rng.normal(0, 0.02, data[:, 1:].shape)
                path = root / f"raw_{name}.csv"
                np.savetxt(path, data, delimiter=",")
                logs.append(str(path))
            env = dict(
                os.environ,
                MPLCONFIGDIR=str(root / "mpl"),
                PYTHONPYCACHEPREFIX=str(root / "bytecode"),
                OPENBLAS_NUM_THREADS="1",
                OMP_NUM_THREADS="1",
            )
            cases = [
                (
                    f"shaper{frequency}",
                    "calibrate_shaper.py",
                    ["-f", str(frequency), logs[0]],
                )
                for frequency in (100, 200, 300)
            ] + [
                ("belts", "graph_belts.py", ["--offline", "-n", *logs]),
                ("spectrogram", "graph_belts.py", ["--offline", *logs]),
            ]
            for name, script, args in cases:
                with self.subTest(name=name):
                    output = root / f"{name}.png"
                    result = subprocess.run(
                        [
                            sys.executable,
                            str(SCRIPTS / script),
                            "-o",
                            str(output),
                            *args,
                        ],
                        env=env,
                        text=True,
                        capture_output=True,
                        timeout=180,
                        check=False,
                    )
                    self.assertEqual(
                        result.returncode, 0, result.stdout + result.stderr
                    )
                    with Image.open(output) as image:
                        image.load()
                        self.assertEqual(image.format, "PNG")
                        self.assertGreater(image.width, 100)
                        self.assertGreater(image.height, 100)


if __name__ == "__main__":
    unittest.main()
