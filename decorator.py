def safe_eval_decorator(func):
    def wrapper(expression):
        try:
            safe_globals = {"__builtins__": None}
            safe_locals = {}

            return func(expression, safe_globals, safe_locals)
        except Exception as e:
            return f"Error: {e}"
    return wrapper


@safe_eval_decorator
def calculate(expression, g, l):
    return eval(expression, g, l)
