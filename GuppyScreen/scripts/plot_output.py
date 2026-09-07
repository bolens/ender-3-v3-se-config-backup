"""Preserve previous calibration plots until a replacement has rendered."""

import os
from pathlib import Path
from tempfile import TemporaryDirectory


def save_figure(figure, output, *, default_format="png"):
    target = Path(output)
    if not os.path.splitext(str(target))[1].lstrip("."):
        target = Path(str(target).rstrip(".") + "." + default_format)
    with TemporaryDirectory(prefix=".guppy-plot-", dir=target.parent) as tmp:
        staged = Path(tmp) / target.name
        figure.savefig(staged)
        staged.replace(target)
    return target
