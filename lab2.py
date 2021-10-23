class MyClass(dict):
    def __init__(self, d):
        self._d = d if d is not None else {}

    def join_keys(self):
        return "".join(self._d.keys())


d1 = {
    "a": [1, 2],
    "b": [3, 4],
    "c": [5, 6]
}

d2 = {
    "  ": [],
    "123": [532, 0],
    ",_,": [0, 1, 0, -1]
}

d3 = {
    "aaa": [-11111],
    "bbb": [2, 4, 3],
    "ccc": [1, 1, 1, 1]
}


print(MyClass(d1).join_keys())
print(MyClass(d2).join_keys())
print(MyClass(d3).join_keys())
