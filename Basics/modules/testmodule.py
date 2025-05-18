def add(a,b):
    return a+b

# mymodules.py
class MyClass:
    def __init__(self):
        pass
    def __mymind__(self):
        return f"Hello"
    def greet(self, name):
        return f"Hello, {name}!"




# Optional test
if __name__ == "__main__":
    print("MyClass module loaded")
    obj = MyClass()
    print(obj.greet("Test"))
