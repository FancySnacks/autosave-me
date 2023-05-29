"""Argument parser"""

from argparse import ArgumentParser
from typing import Sequence


class ArgParser:
    def __init__(self):
        self._parser = ArgumentParser(prog="Autosave-me",
                                      usage="autosave [args]",
                                      description="Autosave is a script that automatically creates 'ctrl-s' input event"
                                                  " to save current work")
        self._args = {}

        self._setup_args()

    def parse_args(self, args: Sequence[str]):
        self.args = self._parser.parse_args(args)

    @property
    def args(self) -> dict:
        return vars(self._args)

    @args.setter
    def args(self, value):
        self._args = value

    def _setup_args(self):
        self._parser.add_argument("-t",
                                  "--time",
                                  type=int,
                                  default=60,
                                  help="Time between each autosave in seconds")
