| Category | Data Type | Class Name | Mutable | Example |
| :--- | :--- | :--- | :--- | :--- |
| **Text** | String | `str` | No | `"Hello"` |
| **Numeric** | Integer | `int` | No | `42` |
| | Floating-point | `float` | No | `3.14` |
| | Complex | `complex` | No | `2 + 3j` |
| **Sequence** | List | `list` | Yes | `[1, 2, 3]` |
| | Tuple | `tuple` | No | `(1, 2, 3)` |
| | Range | `range` | No | `range(5)` |
| **Mapping** | Dictionary | `dict` | Yes | `{"key": "value"}` |
| **Set** | Set | `set` | Yes | `{1, 2, 3}` |
| | Frozen Set | `frozenset` | No | `frozenset({1, 2})` |
| **Boolean** | Boolean | `bool` | No | `True` or `False` |
| **None** | Null Value | `NoneType` | No | `None` |


The True Python Classification: Mutability Instead of "primitive vs. non-primitive," Python developers group data types by Mutability (whether the data can change after it is created).
🔒 Immutable (Cannot Be Changed)When you modify an immutable object, Python does not change the original value. It creates a brand-new object somewhere else in memory and updates the variable to point to it. int, float, complex, str, tuple, bool, frozenset

🔓 Mutable (Can Be Changed)These objects can be modified directly in memory without changing their address location. list, dict, set, bytearray 