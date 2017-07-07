


def tags(tag):
    def inner_decorator(func):
        # kazdy dekorator musi miec wrapper:
        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)

            return f"<{tag}>{result}</{tag}>"

        return wrapper
    return inner_decorator



@tags("div")
@tags("span")
def core_string(name):
    return f"Hello {name}"

print(core_string("Kamczung"))