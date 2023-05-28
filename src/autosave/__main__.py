#!/usr/bin/env python3

from autosave.app import App


def main() -> int:
    timer = App()
    timer.start_timer()

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
