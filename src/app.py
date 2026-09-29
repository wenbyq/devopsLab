def greet(name: str, greeting: str = "Hello"):
    if not name:
        return f"{greeting}, stranger"
    return f"{greeting}, {name}"


def process(data):
    result = data.upper()
    return result
