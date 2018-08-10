def merge_two_dicts(x, y):
        z = x.copy()   # start with x's keys and values
        z.update(y)    # modifies z with y's keys and values & returns None
        return z

def without_callable(props):
    return {x: props[x] for x in props if not callable(props[x])}

def with_callable(props):
    return {x: props[x] for x in props if callable(props[x])}

def find(collection, predicate, callback=None, default=None):
    if callback is None:
        return next((item for item in collection if predicate == item), default)
    else:
        return next((item for item in collection if callback(predicate, item)), default)

def includes(collection, predicate, callback=None):
    if callback is None:
        return next((True for item in collection if predicate == item), False)
    else:
        return next((True for item in collection if callback(predicate, item)), False)