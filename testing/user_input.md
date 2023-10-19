# Pytest Recipies for dealing with user input

### Testing a function with user input

```python
from io import StringIO

def my_func():
    name = input("enter your name")
    return name.title()

def test_my_func(monkeypatch):
    name = StringIO("jeff smith\n")
    monkeypatch.setattr("sys.stdin", name)
    assert my_func() == "Jeff Smith"
```
