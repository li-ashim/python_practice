from contextlib import ContextDecorator
import datetime


class LogFile(ContextDecorator):
    def __init__(self, log_file_name) -> None:
        self.log_file_name = log_file_name
        self.start = None

    def __enter__(self):
        self.start = datetime.datetime.now()
        self.handler = open(self.log_file_name, 'a')
        return self.handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        runtime = datetime.datetime.now() - self.start
        log_str = (f'Start: {self.start.isoformat(sep=" ")} | ' + 
                   f'Run: {str(runtime)} | An error occurred: {exc_val}\n')
        self.handler.write(log_str)
        self.handler.close()
        del self.handler

@LogFile('my_trace.log')
def test_func():
    b = 1 / 0