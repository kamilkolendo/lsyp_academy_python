from functools import wraps


def tags(tag):
    def inner_decorator(func):
        # kazdy dekorator musi miec wrapper:
        @wraps(func) # <- zwiazane z tamtym importem na górze^
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