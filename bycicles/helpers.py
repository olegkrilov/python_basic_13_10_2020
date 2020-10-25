def as_function (obj, *args):
    return obj(*args) if callable(obj) else obj