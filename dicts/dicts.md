# Access values safely in a nested dictionary
```python
from functools import reduce

def nested_get(d: dict, keys:str, default= None):
    if isinstance(keys, list):
        keys = keys

    if isinstance(keys, str):
        keys = keys.split(".")
    
    return reduce(
        lambda d, key: d.get(key) if isinstance(d, dict) else default,
        keys,
        d
    )
```

# Custom sort order
```python
example_dict = {"MAX": 3, "MOD": 2, "MIN": 1}

# want sort order to be MIN, MOD, MAX
{k: example_dict[k] for k in ["MIN", "MOD", "MAX"] if k in example_dict}
```
