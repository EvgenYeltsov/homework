from datetime import datetime
from functools import wraps

def write_logs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return1 = func(*args, **kwargs)
        time_1 = str(datetime.now())
        with open('logs.txt', 'a') as log_file:
            log_info = f"Function name< {func.__name__}>  time <{time_1[:19]}> Result <{return1}>,'\n'"
            log_file.write(log_info)
        return return1
    return wrapper

@write_logs
def get_full_name(name, lastname):
    result = f"{name}{lastname}"
    print(f"Result : {result}")
    return result

get_full_name('A', 'B')