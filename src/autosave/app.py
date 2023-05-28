import keyboard

from autosave.timer import Timer


class App:
    def __init__(self, delay: int = 3):
        self.delay = delay
        self.timer = Timer(delay=delay, parent=self)

    def start_timer(self):
        self.timer.set_timer()

    def event_timer_reset(self):
        self._print_begin_msg()

    def event_save(self):
        App.autosave()
        self._print_saved_msg()

    @staticmethod
    def autosave():
        keyboard.press_and_release('ctrl+s')

    def _print_saved_msg(self):
        print('[autosave-me] Autosave!')

    def _print_begin_msg(self):
        print(f'[autosave-me] Next autosave in {self.delay} second(s) ({self.timer.save_time_estimated()})')
        print("[autosave-me] Press 'ctrl-c' to cancel timer")