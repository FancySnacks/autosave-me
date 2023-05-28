import keyboard

import time
import datetime


class Timer:
    def __init__(self, delay: int = 60, active: bool = True):
        self.delay = delay
        self.active = active

        self._set_timer()

    @property
    def start_time(self) -> float:
        return self._start_time

    @property
    def elapsed_time(self) -> float:
        elapsed = time.time() - self._start_time
        formatted: str = f'{elapsed:.3f}'
        return float(formatted)

    def _set_timer(self):
        self._start_time = time.time()
        self._print_begin_msg()

        while self.active:
            if self._time_to_save():
                Timer.save_call()
                self._print_saved_msg()
                self._print_begin_msg()
                self._reset_timer()

    def _reset_timer(self):
        self._start_time = time.time()

    def _time_to_save(self) -> bool:
        return self.elapsed_time == float(self.delay)

    def _save_time_estimated(self):
        now = datetime.datetime.now()
        return now + datetime.timedelta(seconds=self.delay)

    @staticmethod
    def save_call():
        keyboard.press_and_release('ctrl+s')

    def _print_saved_msg(self):
        print('[autosave-me] Autosave!')

    def _print_begin_msg(self):
        print(f'[autosave-me] Next autosave in {self.delay} second(s) ({self._save_time_estimated().strftime("%H:%M:%S %Y-%m-%d")})')
        print("[autosave-me] Press 'ctrl-c' to cancel timer")
