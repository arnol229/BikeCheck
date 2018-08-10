def merge_two_dicts(x, y):
        z = x.copy()   # start with x's keys and values
        z.update(y)    # modifies z with y's keys and values & returns None
        return z

def without_callable(props):
    return {x: props[x] for x in props if not callable(props[x])}

def with_callable(props):
    return {x: props[x] for x in props if callable(props[x])}