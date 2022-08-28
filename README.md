### Json File Descriptor in Python ###

This is a simple json file descriptor. It can describe the the simple and nested json file. 

#### Basic Usage ####

```python
from dot_json import describe_json_file

result = describe_json_file(file_path="Your file path")

print(result)
```

#### Run Examples ####

```terminal
$ python examples/example1.py
```
##### OUTPUT #####
```json
{"type": "dict", "length": 6, "keys": {"name": {"type": "str", "length": 13}, "profession": {"type": "str", "length": 8}, "specialization": {"type": "str", "length": 17}, "skills": {"type": "list", "length": 3, "items": {"type": "dict", "length": 2, "keys": {"skill": {"type": "str", "length": 15}, "experience": {"type": "str", "length": 7}}}}, "address": {"type": "dict", "length": 2, "keys": {"permanent": {"type": "str", "length": 36}, "temporary": {"type": "str", "length": 38}}}, "education": {"type": "list", "length": 3, "items": {"type": "dict", "length": 3, "keys": {"level": {"type": "str", "length": 12}, "program": {"type": "str", "length": 23}, "year": {"type": "str", "length": 9}}}}}}
```