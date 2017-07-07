l = [1,2,3]

a,c,b=l

kw = {"a": 23,
      "b": 24,
      "c": 25}

def func(a, b, c):
    print(f"First arg {a}")
    print(f"Second arg {b}")
    print(f"Third arg {c}")

func(*l)
func(**kw)