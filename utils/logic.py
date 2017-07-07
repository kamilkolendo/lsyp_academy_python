y = True
n = False

def get_full_name(name, default="Gonzales"):
    first_name = "Juan"
    last_name = name or default #FUNFACT
    return f"{first_name} {last_name}"

print(get_full_name("Kolendo"))