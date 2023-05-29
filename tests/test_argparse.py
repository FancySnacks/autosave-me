import pytest

from autosave.parser import ArgParser


@pytest.mark.parametrize("args, key, expected", [
    (['-t 30'], 'time', 30)
])
def test_parses_args_from_list_of_strings(args: str, key: str, expected):
    parser = ArgParser()
    parser.parse_args(args)
    print(parser.args)
    assert parser.args[key] == expected


def test_exception_when_passing_unknown_args():
    with pytest.raises(SystemExit):
        args = ["-n"]
        parser = ArgParser()
        parser.parse_args(args)
