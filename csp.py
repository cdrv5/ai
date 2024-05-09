V = ["A", "B", "C", "D", "E", "F", "G"]
C = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("B", "E"), ("C", "E"), ("C", "F"), ("D", "E"), ("E", "F"), ("E", "G"), ("F", "G")]
D = ["red", "pink", "purple"]

def backtrack(a={}):
    if len(a) == len(V): 
        return a
    v = next((x for x in V if x not in a), None)
    for d in D:
        if all(d != a.get(x) for x, y in C if y == v) and backtrack({**a, v: d}):
            return backtrack({**a, v: d})
    return None

def main():
    return backtrack()

if _name_ == "_main_":
    result = main()
    if result:
        for vertex, color in result.items():
            print(f"Vertex {vertex} is assigned color {color}")
    else:
        print("No valid coloring found.")
