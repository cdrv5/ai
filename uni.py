def unify(x, y):
    if x == y:
        return {}
    elif isinstance(x, str) and x.islower():
        return {x: y}
    elif isinstance(y, str) and y.islower():
        return {y: x}
    elif isinstance(x, list) and isinstance(y, list):
        return unify_lists(x, y)
    else:
        return None

def unify_lists(x, y):
    if not x or not y:
        return {}
    theta = unify(x[0], y[0])
    if theta is None:
        return None
    theta_prime = unify(x[1:], y[1:])
    if theta_prime is None:
        return None
    theta.update(theta_prime)
    return theta

# Example usage
facts1 = ["likes", "John", "apples"]
facts2 = ["likes", "X", "apples"]
unification_result = unify(facts1, facts2)
print("Unification result:", unification_result)
