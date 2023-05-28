"""Timer class for doing scheduled tasks"""

import time
import datetime

from typing import Protocol


class TimerEvent(Protocol):
    """
    Provides interface for scheduled timer events

    event_timer_elapsed()
    vent_timer_reset()
    """
    def event_timer_elapsed(self):
        ...

    def event_timer_reset(self):
        ...


class Timer:
    """
    Timer class with scheduled task.

    parent: TimerEvent
        an object that implements 'TimerEvent' protocol
    """

    def __init__(self, parent: TimerEvent):
        self.parent = parent

    @property
    def start_time(self) -> float:
        return self._start_time

    @property
    def elapsed_time(self) -> float:
        elapsed = time.time() - self._start_time
        formatted: str = f'{elapsed:.3f}'
        return float(formatted)

    def set_timer(self, delay: int):
        self.active = True
        self.delay = delay
        self._reset_timer()

        while self.active:
            try:
                if self._is_it_time():
                    self.parent.event_timer_elapsed()
                    self._reset_timer()
            except KeyboardInterrupt as e:
                return 1

    def _reset_timer(self):
        self._start_time = time.time()
        self.parent.event_timer_reset()

    def _is_it_time(self) -> bool:
        return self.elapsed_time == float(self.delay)

    def save_time_estimated(self) -> str:
        """
        Target time of an upcoming scheduled task

        format:
        '%H:%M:%S %Y-%m-%d'
        """
        now = datetime.datetime.now()
        t = now + datetime.timedelta(seconds=self.delay)
        return t.strftime("%H:%M:%S %Y-%m-%d")
