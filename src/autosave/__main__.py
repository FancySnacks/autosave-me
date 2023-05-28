#!/usr/bin/env python3

from autosave.app import App
from autosave.timer import Timer


def main() -> int:
    app = App()
    timer = Timer(parent=app)
    app.start_timer(timer)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
