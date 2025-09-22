# print
#
# some = print
#
# some(555)
# print(some, 555555555)
# print(print, 555555555)
# print(print(), 555555555)
#
# print(id(some))
# print(id(print), 55555555555)
from typing import Callable


def foo(number: int = 6) -> int:
    print(33333333)
    return number + 5


def foo2(arg: str = "kkkk") -> str:
    print(66666666)
    return arg * 2


def foo3() -> str:
    print(100000000000000)
    return 'Hello buddy'


def foo4(arg_1: int, arg_2: int) -> int:
    print(99999999999)
    return arg_1 + arg_2


def call_callable_function(func: Callable, *args, **kwargs):
    print(4444444444444)
    print(args)
    print(kwargs)

    result = func(*args, **kwargs)  # foo()
    print(func, "---->>>", result)
    # print(int("000001D7E36EA2A0", 16))
    return result


# call_callable_function(func=foo, number=55)
# call_callable_function(foo2, 'ggggg')
# # call_callable_function(func=foo2)
# call_callable_function(foo3)
# call_callable_function(foo4, 15, 35)


# #################################################################################################

def call_callable_function_master(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print(232323232)
        print(args, kwargs)
        print(func)
        pass

    return inner

res = call_callable_function_master(func=foo)

res(b=555)
