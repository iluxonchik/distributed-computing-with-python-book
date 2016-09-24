# There are 3 main constructs in coroutines:
# * yield - used to suspend the execution of the routine
# * send() - used to pass data into the routine (and resume its execution)
# * close() - used to terminate a courotine

from functools import wraps

def complain_about(substring):
    print('Talk to me')
    try:
        while True:
            text = yield
            if substring in text:
                print('Ayo, I found {} again!'.format(substring))
    except GeneratorExit:
        print('Aight, qutting, cya later alligator!')

def coroutine(fn):
    @wraps
    def wrapper(*args, **kwargs):
        c = fn(*args, **kwargs)  # create a new generator object
        next(c)  # activate the generator object
        return c
    return wrapper

@coroutine
def complain_about_2(substring):
    print('Talk to me')
    try:
        while True:
            text = yield
            if substring in text:
                print('Ayo, I found {} again!'.format(substring))
    except GeneratorExit:
        print('Aight, quittng, cya later alligator!')

