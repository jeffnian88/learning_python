def foo():
    # do something
    print 'hello in foo()'

def decorator(func):
    # manipulate func
    print 'hello in decorator()'
    return func

foo = decorator(foo)  # Manually decorate

foo()

@decorator
def bar():
    # Do something
    print 'hello in bar()'
# bar() is decorated

bar()
bar()
