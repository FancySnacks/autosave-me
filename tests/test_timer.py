import pytest

import datetime

from threading import Thread

from autosave.timer import Timer


class MockTimerParent:
    def __init__(self):
        self.elapsed_func_called = False
        self.reset_func_called = False

    def event_timer_elapsed(self):
        self.elapsed_func_called = True

    def event_timer_reset(self):
        self.reset_func_called = True


@pytest.fixture
def mock_parent() -> MockTimerParent:
    return MockTimerParent()


@pytest.fixture
def timer(mock_parent) -> Timer:
    return Timer(mock_parent)


def test_timer_estimated_save_time_is_correct(timer: Timer):
    timer.delay = 30
    expected = datetime.datetime.now() + datetime.timedelta(seconds=30)
    expected_formatted = expected.strftime("%H:%M:%S")
    estimated_save_time = timer.save_time_estimated(time_format="%H:%M:%S")
    assert estimated_save_time == expected_formatted


def test_timer_calls_event_on_timer_elapsed_successfully(timer: Timer):
    timer.call_timer_elapsed_event()
    assert timer.parent.elapsed_func_called is True


def test_timer_calls_event_on_timer_reset_successfully(timer: Timer):
    timer.call_timer_reset_event()
    assert timer.parent.reset_func_called is True


def test_timer_calls_event_on_timer_elapsed_after_delay(timer: Timer):
    timer.set_timer(delay=1, do_once=True)
    assert timer.parent.elapsed_func_called is True


def test_timer_is_cancelled(timer: Timer):
    timer._cancel_timer()
    assert timer.active is False
