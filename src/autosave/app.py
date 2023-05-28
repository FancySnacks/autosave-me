"""Class that controls and manages entirety of this program"""

import keyboard


class App:
    def start_timer(self, timer, delay: int = 60):
        self.timer = timer
        self.timer.set_timer(delay)

    def event_timer_reset(self):
        self._print_begin_msg()

    def event_timer_elapsed(self):
        App.autosave()
        self._print_saved_msg()

    @staticmethod
    def autosave():
        keyboard.press_and_release('ctrl+s')

    def _print_saved_msg(self):
        print('[autosave-me] Autosave!')

    def _print_begin_msg(self):
        print(f'[autosave-me] Next autosave in {self.timer.delay} second(s) ({self.timer.save_time_estimated()})')
        print("[autosave-me] Press 'ctrl-c' to cancel timer")