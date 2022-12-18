def double_args(func):
    def wrapper(a, b):
        return func(a * 2, b * 2)
    return wrapper


@double_args
def multiply(a, b):
    return a * b


multiply

print(multiply)


print(multiply(1, 5))
