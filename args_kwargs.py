def foobar(a, *args, **kwargs):
    print(f"a = {a}, b = {kwargs['b']}, args = {args}, kwargs = {kwargs}")


foobar(8, 10, 11, 12, 13, 14, 16, b=17, c=18)