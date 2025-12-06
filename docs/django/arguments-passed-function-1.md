# Packing arguments

Here's a clear and practical explanation of `*`, `*args`, and `**kwargs` in Python functions:

### 1. `*` – The unpacking / packing operator

The asterisk `*` has two main uses in function definitions:

#### In function definition: Packing arguments
```python
def my_function(*args):
    print(args)        # args is a tuple
    for arg in args:
        print(arg)

my_function(1, 2, 3, "hello")
# Output:
(1, 2, 3, 'hello')
1
2
3
hello
```

`*args` collects all positional arguments into a tuple.

You can name it anything, but `*args` is the convention:
```python
def func(*anything):
    print(anything)

func(10, 20)  # (10, 20)
```

#### In function call: Unpacking arguments
```python
numbers = [1, 2, 3, 4]

print(numbers)     # [1, 2, 3, 4]
print(*numbers)    # 1 2 3 4   ← unpacks the list
```

### 2. `**` – For keyword arguments

#### In function definition: Packing keyword arguments
```python
def my_function(**kwargs):
    print(kwargs)           # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key} = {value}")

my_function(name="Alice", age=30, city="Paris")
# Output:
{'name': 'Alice', 'age': 30, 'city': 'Paris'}
name = Alice
age = 30
city = Paris
```

`kwargs` stands for "keyword arguments" – collects them into a dict.

#### In function call: Unpacking dictionary into keyword arguments
```python
config = {"sep": " → ", "end": "!!!\n"}

print("hello", "world", **config)
# Output: hello → world!!!
```

### 3. Combining everything (correct order!)

```python
def example(a, b, *args, c=10, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("c =", c)
    print("kwargs =", kwargs)

# Call it
example(1, 2, 3, 4, 5, c=100, x=7, y=8)
```

Output:
```
a = 1
b = 2
args = (3, 4, 5)           ← extra positional args
c = 100                    ← explicit keyword overrides default
kwargs = {'x': 7, 'y': 8}   ← extra keyword args
```

Important order in function definition:
```python
def func(pos1, pos2, /, pos_or_kwd, *, kw_only1, **kwargs):
    ...
```
But most common and flexible pattern:
```python
def my_func(param1, param2, *args, kwparam=10, **kwargs):
    ...
```

### Real-world examples

```python
# Like print() uses them
print("a", "b", "c", sep="-", end="!\n")

# Passing arguments to another function
def wrapper(*args, **kwargs):
    print("Before")
    original_function(*args, **kwargs)
    print("After")

# Django views, Flask routes, decorators all use *args/**kwargs heavily
```

### Summary Table

| Syntax       | In definition                  | In call                     | Type inside function |
|--------------|-------------------------------|----------------------------|----------------------|
| `*args`      | Packs extra positional args   | Unpacks iterable into args | `tuple`             |
| `**kwargs`   | Packs extra keyword args      | Unpacks dict into kwargs  | `dict`              |
| `*` alone    | Forces following params to be keyword-only | Unpacks iterable        | —                   |
| `**` alone   | —                             | Unpacks mapping            | —                   |

Now you can read and write any Python function signature confidently! 🚀