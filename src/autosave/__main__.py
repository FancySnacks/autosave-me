#!/usr/bin/env python3

from typing import Sequence

from autosave.app import App
from autosave.timer import Timer
from autosave.parser import ArgParser


def main(argv: Sequence[str] | None = None) -> None:
    parser = ArgParser()
    parser.parse_args(argv)

    app = App()
    timer = Timer(app)

    app.start_timer(timer, delay=parser.args['time'])


if __name__ == '__main__':
    raise SystemExit(main())
