import time
import datetime


class Timer:
    def __init__(self, delay: int, parent):
        self.delay = delay
        self.parent = parent

    @property
    def start_time(self) -> float:
        return self._start_time

    @property
    def elapsed_time(self) -> float:
        elapsed = time.time() - self._start_time
        formatted: str = f'{elapsed:.3f}'
        return float(formatted)

    def set_timer(self):
        self.active = True
        self._reset_timer()

        while self.active:
            try:
                if self._time_to_save():
                    self.parent.event_save()
                    self._reset_timer()
            except KeyboardInterrupt as e:
                return 1

    def _reset_timer(self):
        self._start_time = time.time()
        self.parent.event_timer_reset()

    def _time_to_save(self) -> bool:
        return self.elapsed_time == float(self.delay)

    def save_time_estimated(self) -> str:
        now = datetime.datetime.now()
        t = now + datetime.timedelta(seconds=self.delay)
        return t.strftime("%H:%M:%S %Y-%m-%d")
