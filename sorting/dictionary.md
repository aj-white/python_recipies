## Sort a dictionary by values in one line
This handy tip comes from [this medium article](https://itnext.io/8-extremely-useful-python-one-liners-for-your-next-project-7fdb01b4ee23)

```python
sorted_data = {key:data[key] for key in sorted(data, key=data.get)}
```
