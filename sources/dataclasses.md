## Python `dataclasses` in Python 3.14

This note explains how the `@dataclass` decorator works, the default dataclass parameters, and the behavior of `init`, `frozen`, and `slots` in detail.

The official Python documentation defines `@dataclass` as a decorator that adds generated special methods to user-defined classes based on annotated fields. In Python 3.14, the decorator signature is:

```python
@dataclass(
    *,
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
    match_args=True,
    kw_only=False,
    slots=False,
    weakref_slot=False,
)
class C:
    ...
```

Source: Python documentation, `dataclasses` module: <https://docs.python.org/3/library/dataclasses.html>

---

## 1. What `@dataclass` does

A dataclass is an ordinary Python class with boilerplate methods generated automatically from annotated fields.

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
```

This is conceptually similar to writing:

```python
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return (
            f"Book(title={self.title!r}, "
            f"author={self.author!r}, "
            f"year={self.year!r})"
        )

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.title, self.author, self.year) == (
                other.title,
                other.author,
                other.year,
            )
        return NotImplemented
```

Example:

```python
b1 = Book("The Trial", "Franz Kafka", 1925)
b2 = Book("The Trial", "Franz Kafka", 1925)

print(b1)
print(b1 == b2)
```

Output:

```text
Book(title='The Trial', author='Franz Kafka', year=1925)
True
```

---

## 2. Annotated attributes become dataclass fields

The central rule is that dataclasses use type annotations to identify fields.

```python
@dataclass
class Student:
    name: str
    age: int
```

Here, `name` and `age` are dataclass fields.

An unannotated class attribute is not a dataclass field:

```python
@dataclass
class Student:
    name: str
    age: int
    school = "RTU"
```

The generated constructor is conceptually:

```python
def __init__(self, name: str, age: int):
    self.name = name
    self.age = age
```

`school` remains accessible, but it is not part of the generated constructor or generated representation.

```python
s = Student("Anna", 21)

print(s)
print(s.school)
```

Output:

```text
Student(name='Anna', age=21)
RTU
```

---

## 3. Type annotations are not runtime validation

Dataclasses use annotations to know which fields exist. They do not normally enforce the annotated types at runtime.

```python
@dataclass
class Student:
    name: str
    age: int

s = Student("Anna", "twenty-one")
```

This is allowed by Python at runtime, even though `age` is annotated as `int`.

The annotations are useful for:

- static type checkers such as `mypy` or `pyright`;
- IDE autocompletion and diagnostics;
- generated constructor signatures;
- documentation and readability.

They are not automatic validators.

For runtime validation, use `__post_init__`:

```python
@dataclass
class Student:
    name: str
    age: int

    def __post_init__(self):
        if not isinstance(self.age, int):
            raise TypeError("age must be int")
```

---

## 4. Default values

Defaults work like normal Python function defaults.

```python
@dataclass
class Student:
    name: str
    age: int = 18
```

This allows:

```python
Student("Anna")
Student("Anna", 21)
```

The generated initializer is roughly:

```python
def __init__(self, name: str, age: int = 18):
    self.name = name
    self.age = age
```

The usual Python rule applies: non-default parameters cannot follow default parameters.

This is invalid:

```python
@dataclass
class BadStudent:
    age: int = 18
    name: str
```

It raises `TypeError`, because a required field follows a field with a default.

This rule also applies through inheritance.

---

## 5. Mutable defaults and `default_factory`

Do not use mutable objects such as lists, dictionaries, or sets as direct defaults.

Incorrect:

```python
@dataclass
class Course:
    students: list[str] = []
```

Correct:

```python
from dataclasses import dataclass, field

@dataclass
class Course:
    students: list[str] = field(default_factory=list)
```

Now each instance receives its own list.

```python
c1 = Course()
c2 = Course()

c1.students.append("Anna")

print(c1.students)
print(c2.students)
```

Output:

```text
['Anna']
[]
```

`default_factory` must be a zero-argument callable.

---

## 6. `field()` customization

Use `field()` when a plain annotation or default is not enough.

```python
from dataclasses import dataclass, field

@dataclass
class User:
    username: str
    password_hash: str = field(repr=False)
```

Now `password_hash` is omitted from `repr`:

```python
u = User("val", "abc123hash")
print(u)
```

Output:

```text
User(username='val')
```

Common `field()` options include:

```python
field(default=...)
field(default_factory=...)
field(init=False)
field(repr=False)
field(compare=False)
field(kw_only=True)
field(metadata={...})
```

Example with comparison disabled for one field:

```python
@dataclass
class Article:
    title: str
    word_count: int
    internal_id: int = field(compare=False)

print(Article("A", 1000, 1) == Article("A", 1000, 2))
```

Output:

```text
True
```

---

## 7. Default `@dataclass` parameter values

The default values are:

```python
@dataclass(
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
    match_args=True,
    kw_only=False,
    slots=False,
    weakref_slot=False,
)
class C:
    ...
```

| Parameter | Default | Meaning |
|---|---:|---|
| `init` | `True` | Generate `__init__()` from dataclass fields. |
| `repr` | `True` | Generate `__repr__()`. |
| `eq` | `True` | Generate `__eq__()`. |
| `order` | `False` | Do not generate ordering methods unless requested. |
| `unsafe_hash` | `False` | Do not force-generate `__hash__()` unsafely. |
| `frozen` | `False` | Instances are mutable by default. |
| `match_args` | `True` | Generate `__match_args__` for structural pattern matching. |
| `kw_only` | `False` | Fields are not keyword-only by default. |
| `slots` | `False` | Do not generate `__slots__` by default. |
| `weakref_slot` | `False` | Do not add a `__weakref__` slot by default. |

So this:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

means the same as:

```python
from dataclasses import dataclass

@dataclass(
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
    match_args=True,
    kw_only=False,
    slots=False,
    weakref_slot=False,
)
class Point:
    x: int
    y: int
```

---

## 8. `init=True`

`init=True` is the default. It tells the dataclass decorator to generate an `__init__()` method.

```python
from dataclasses import dataclass

@dataclass(init=True)
class Student:
    name: str
    age: int
    active: bool = True
```

The generated initializer is roughly:

```python
def __init__(self, name: str, age: int, active: bool = True):
    self.name = name
    self.age = age
    self.active = active
```

Usage:

```python
s1 = Student("Anna", 21)
s2 = Student("Peter", 22, False)

print(s1)
print(s2)
```

Output:

```text
Student(name='Anna', age=21, active=True)
Student(name='Peter', age=22, active=False)
```

### 8.1 Only annotated fields become constructor parameters

```python
@dataclass
class Book:
    title: str
    year: int
    category = "fiction"
```

The generated initializer is roughly:

```python
def __init__(self, title: str, year: int):
    self.title = title
    self.year = year
```

`category` is not included because it has no annotation.

### 8.2 `init=False` on the whole dataclass

You can disable generation of `__init__`:

```python
@dataclass(init=False)
class Point:
    x: int
    y: int
```

Now Python does not generate:

```python
def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
```

So this fails unless another initializer exists:

```python
p = Point(1, 2)
```

You would need to define initialization yourself:

```python
@dataclass(init=False)
class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
```

Using `init=False` for the whole class is uncommon. It is mainly useful when:

- you want full manual control over construction;
- you are integrating with an existing framework;
- you want dataclass features such as `repr` and `eq` but not the generated constructor;
- you are doing unusual metaprogramming.

### 8.3 Explicit `__init__` overrides generated `__init__`

If the class already defines `__init__`, dataclasses do not overwrite it.

```python
@dataclass(init=True)
class Student:
    name: str
    age: int

    def __init__(self, name: str):
        self.name = name
        self.age = 0
```

This works:

```python
Student("Anna")
```

This fails:

```python
Student("Anna", 21)
```

### 8.4 Per-field `init=False`

There is also a field-level `init` option.

```python
from dataclasses import dataclass, field

@dataclass
class User:
    username: str
    password_hash: str = field(init=False)
```

The generated initializer is roughly:

```python
def __init__(self, username: str):
    self.username = username
```

`password_hash` is not accepted by the constructor.

A common pattern is to compute such fields in `__post_init__`:

```python
from dataclasses import dataclass, field

@dataclass
class User:
    username: str
    raw_password: str
    password_hash: str = field(init=False)

    def __post_init__(self):
        self.password_hash = f"hashed:{self.raw_password}"
```

### 8.5 `__post_init__`

`__post_init__` runs after the generated initializer has assigned fields.

```python
@dataclass
class Rectangle:
    width: float
    height: float

    def __post_init__(self):
        if self.width <= 0:
            raise ValueError("width must be positive")
        if self.height <= 0:
            raise ValueError("height must be positive")
```

Prefer `__post_init__` over writing a manual `__init__` unless full manual construction is necessary.

### 8.6 `InitVar`

`InitVar` creates a constructor parameter that is passed to `__post_init__` but is not stored as a normal field.

```python
from dataclasses import dataclass, InitVar, field

@dataclass
class User:
    username: str
    password: InitVar[str]
    password_hash: str = field(init=False)

    def __post_init__(self, password):
        self.password_hash = f"hashed:{password}"
```

Usage:

```python
u = User("val", "secret")

print(u.username)
print(u.password_hash)
```

But `u.password` does not exist as a normal instance attribute.

---

## 9. `repr=True`

`repr=True` is the default. It generates a readable `__repr__()` method.

```python
@dataclass
class Point:
    x: int
    y: int

print(Point(1, 2))
```

Output:

```text
Point(x=1, y=2)
```

You can exclude a field from the generated representation:

```python
@dataclass
class User:
    username: str
    password_hash: str = field(repr=False)
```

---

## 10. `eq=True`

`eq=True` is the default. It generates `__eq__()`.

```python
@dataclass
class Point:
    x: int
    y: int

print(Point(1, 2) == Point(1, 2))
```

Output:

```text
True
```

Equality compares fields as if they were a tuple, and both objects must be of the identical class.

---

## 11. `order=False`

`order=False` is the default. Ordering methods are not generated unless explicitly requested.

```python
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

print(Version(1, 2, 0) < Version(1, 3, 0))
```

Output:

```text
True
```

Ordering is tuple-like:

```python
(1, 2, 0) < (1, 3, 0)
```

If `order=True` but `eq=False`, dataclasses raise `ValueError`.

---

## 12. `frozen=False` and `frozen=True`

`frozen=False` is the default, so dataclass instances are mutable.

```python
@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
p.x = 10
```

With `frozen=True`, ordinary attribute assignment and deletion are blocked.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
p.x = 10
```

This raises:

```text
dataclasses.FrozenInstanceError: cannot assign to field 'x'
```

`FrozenInstanceError` is a subclass of `AttributeError`.

### 12.1 How frozen is enforced

`frozen=True` is enforced by generated `__setattr__` and `__delattr__` methods. Conceptually, the class behaves as if it had:

```python
def __setattr__(self, name, value):
    raise FrozenInstanceError(f"cannot assign to field {name!r}")

def __delattr__(self, name):
    raise FrozenInstanceError(f"cannot delete field {name!r}")
```

Ordinary assignment:

```python
p.x = 5
```

internally calls:

```python
p.__setattr__("x", 5)
```

and the generated method rejects it.

### 12.2 How initialization works in a frozen dataclass

A frozen dataclass cannot initialize fields using normal assignment, because that would trigger the generated blocking `__setattr__`.

Instead, the generated initializer uses `object.__setattr__` internally:

```python
object.__setattr__(self, "x", x)
object.__setattr__(self, "y", y)
```

Construction is allowed; later ordinary assignment is blocked.

### 12.3 Frozen is shallow, not deep

`frozen=True` prevents rebinding attributes. It does not recursively freeze the objects stored in those attributes.

```python
@dataclass(frozen=True)
class Basket:
    items: list[str]

b = Basket(["apple", "banana"])
```

This fails:

```python
b.items = ["orange"]
```

But this succeeds:

```python
b.items.append("orange")
```

The field was not rebound. The existing list object was mutated.

For stronger value-object behavior, use immutable field types:

```python
@dataclass(frozen=True)
class Basket:
    items: tuple[str, ...]
```

### 12.4 Frozen can be bypassed deliberately

Python does not treat `frozen=True` as a security boundary.

```python
object.__setattr__(p, "x", 99)
```

This can mutate a frozen dataclass. It is a deliberate bypass.

Without `slots=True`, a frozen dataclass may also have a `__dict__`, and direct mutation of that dictionary may bypass ordinary assignment checks:

```python
p.__dict__["x"] = 99
```

Combining `frozen=True` with `slots=True` removes the normal per-instance `__dict__`, making this particular bypass unavailable.

### 12.5 `__post_init__` with frozen dataclasses

This fails:

```python
@dataclass(frozen=True)
class User:
    name: str
    normalized_name: str = ""

    def __post_init__(self):
        self.normalized_name = self.name.lower()
```

Correct version:

```python
@dataclass(frozen=True)
class User:
    name: str
    normalized_name: str = ""

    def __post_init__(self):
        object.__setattr__(self, "normalized_name", self.name.lower())
```

### 12.6 Frozen and hashing

With `eq=True` and `frozen=True`, dataclasses usually generate a `__hash__()` method.

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
d = {p: "some value"}
```

This only works safely if all fields are hashable.

This fails:

```python
@dataclass(frozen=True)
class Basket:
    items: list[str]

b = Basket(["apple"])
hash(b)
```

because `list` is unhashable.

---

## 13. `slots=False` and `slots=True`

`slots=False` is the default. Ordinary dataclass instances usually have a per-instance `__dict__`.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p.__dict__)
```

Output:

```text
{'x': 1, 'y': 2}
```

Because the instance has a dictionary, new attributes can be added dynamically:

```python
p.z = 3
print(p.__dict__)
```

Output:

```text
{'x': 1, 'y': 2, 'z': 3}
```

With `slots=True`, dataclasses generate `__slots__` for declared fields.

```python
from dataclasses import dataclass

@dataclass(slots=True)
class Point:
    x: int
    y: int
```

This is conceptually similar to:

```python
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
```

Now fields are stored in fixed slots rather than in a per-instance dictionary.

```python
p = Point(1, 2)
print(Point.__slots__)
```

Output:

```text
('x', 'y')
```

This fails:

```python
p.z = 3
```

because `z` is not a declared slot.

### 13.1 Why use `slots=True`?

Use `slots=True` when you want:

- lower memory usage for many instances;
- a fixed object shape;
- prevention of accidental new attributes;
- somewhat more value-object-like data structures;
- potentially slightly faster attribute access, though this is not usually the main reason.

The most important reason is memory layout. For one object, it rarely matters. For hundreds of thousands or millions of objects, it can matter substantially.

Example:

```python
@dataclass(slots=True)
class Token:
    text: str
    start: int
    end: int
    lemma: str
```

This can be useful for large NLP, parsing, indexing, graph, or tabular workloads.

### 13.2 `slots=True` does not make objects immutable

```python
@dataclass(slots=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
p.x = 100      # allowed
p.z = 3        # not allowed
```

`slots=True` prevents undeclared attributes. It does not prevent mutation of declared fields.

For both fixed layout and ordinary assignment prevention, combine it with `frozen=True`:

```python
@dataclass(frozen=True, slots=True)
class Point:
    x: int
    y: int
```

### 13.3 `slots=True` and defaults

Defaults work normally.

```python
@dataclass(slots=True)
class ServerConfig:
    host: str
    port: int = 8000
    debug: bool = False
```

Usage:

```python
cfg = ServerConfig("localhost")
print(cfg)
```

Output:

```text
ServerConfig(host='localhost', port=8000, debug=False)
```

Slots affect storage, not constructor semantics.

### 13.4 `slots=True` and `field()`

Field options still work normally.

```python
from dataclasses import dataclass, field

@dataclass(slots=True)
class User:
    username: str
    password_hash: str = field(repr=False)
    login_count: int = 0

u = User("val", "abc123")
print(User.__slots__)
print(u)
```

Output:

```text
('username', 'password_hash', 'login_count')
User(username='val', login_count=0)
```

### 13.5 `slots=True` and inheritance

Simple slotted inheritance works:

```python
@dataclass(slots=True)
class Person:
    name: str

@dataclass(slots=True)
class Student(Person):
    student_id: str

s = Student("Anna", "S001")
print(s.name)
print(s.student_id)
```

Inherited fields are not necessarily duplicated in the subclass’s `__slots__`. Therefore, do not use `__slots__` as the canonical way to inspect dataclass fields.

Use `dataclasses.fields()` instead:

```python
from dataclasses import fields

for f in fields(Student):
    print(f.name)
```

Output:

```text
name
student_id
```

### 13.6 Mixing slotted and non-slotted classes

A non-slotted base class may provide a `__dict__`, reducing or eliminating the memory benefit of a slotted subclass.

```python
@dataclass
class Person:
    name: str

@dataclass(slots=True)
class Student(Person):
    student_id: str
```

Likewise, a non-slotted subclass of a slotted base class may reintroduce a `__dict__`.

Practical rule: if you care about fixed layout and memory benefits, use `slots=True` consistently through the relevant hierarchy.

### 13.7 `slots=True` and weak references

A slotted class does not automatically support weak references unless it has a `__weakref__` slot.

With dataclasses, use:

```python
@dataclass(slots=True, weakref_slot=True)
class Node:
    value: int
```

Then:

```python
import weakref

n = Node(10)
r = weakref.ref(n)
print(r())
```

Without `weakref_slot=True`, weak references to instances may fail with:

```text
TypeError: cannot create weak reference to 'Node' object
```

`weakref_slot=True` requires `slots=True`.

### 13.8 `slots=True` and class replacement

When `slots=True`, the dataclass decorator returns a new class rather than merely modifying the original class in place. This usually does not matter in ordinary application code, but it can matter for advanced metaprogramming, subclass hooks, and decorator interactions.

### 13.9 `slots=True` and custom `__slots__`

This is invalid:

```python
@dataclass(slots=True)
class Point:
    __slots__ = ("x", "y")

    x: int
    y: int
```

If `slots=True`, dataclasses generate `__slots__`. Defining your own `__slots__` at the same time raises `TypeError`.

Prefer:

```python
@dataclass(slots=True)
class Point:
    x: int
    y: int
```

### 13.10 `slots=True` and properties

Properties work normally.

```python
@dataclass(slots=True)
class Rectangle:
    width: float
    height: float

    @property
    def area(self) -> float:
        return self.width * self.height

r = Rectangle(10, 5)
print(r.area)
```

Output:

```text
50
```

### 13.11 `slots=True` and cached/computed attributes

Slots can surprise you if you try to attach computed attributes later.

This may fail:

```python
@dataclass(slots=True)
class Document:
    text: str

    def word_count(self) -> int:
        self._word_count = len(self.text.split())
        return self._word_count
```

because `_word_count` was not declared as a slot.

Correct version:

```python
from dataclasses import dataclass, field

@dataclass(slots=True)
class Document:
    text: str
    _word_count: int | None = field(default=None, init=False, repr=False)

    def word_count(self) -> int:
        if self._word_count is None:
            self._word_count = len(self.text.split())
        return self._word_count
```

### 13.12 Strong practical value-object form

A common modern form is:

```python
@dataclass(frozen=True, slots=True)
class Coordinate:
    x: int
    y: int
```

This gives:

- fixed fields;
- no accidental new attributes;
- no ordinary mutation;
- lower memory overhead;
- usually hashability, if all fields are hashable.

For nested values, prefer immutable field types:

```python
@dataclass(frozen=True, slots=True)
class Document:
    title: str
    tags: tuple[str, ...]
    word_count: int
```

---

## 14. `kw_only=False` and keyword-only fields

`kw_only=False` is the default, so fields can normally be passed positionally.

```python
@dataclass
class Server:
    host: str
    port: int

Server("localhost", 8000)
```

With `kw_only=True`:

```python
@dataclass(kw_only=True)
class Server:
    host: str
    port: int
```

The generated initializer is conceptually:

```python
def __init__(self, *, host: str, port: int):
    self.host = host
    self.port = port
```

This fails:

```python
Server("localhost", 8000)
```

Correct:

```python
Server(host="localhost", port=8000)
```

You can also make individual fields keyword-only with `field(kw_only=True)`.

---

## 15. `match_args=True`

`match_args=True` is the default. It generates `__match_args__` for structural pattern matching.

```python
@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)

match p:
    case Point(1, y):
        print(y)
```

Output:

```text
2
```

Keyword-only fields are not included in `__match_args__`.

---

## 16. `unsafe_hash=False`

`unsafe_hash=False` is the default. Dataclasses decide whether to generate `__hash__()` based on the combination of `eq` and `frozen`.

Common cases:

| `eq` | `frozen` | Hash behavior |
|---:|---:|---|
| `True` | `True` | Dataclass usually generates `__hash__()`. |
| `True` | `False` | `__hash__` is set to `None`; instances are unhashable. |
| `False` | either | Dataclass generally leaves superclass hash behavior alone. |

`unsafe_hash=True` forces hash generation even when it may be logically unsafe. It should be used rarely.

A dangerous example:

```python
@dataclass(unsafe_hash=True)
class MutablePoint:
    x: int
    y: int
```

If an instance is used as a dictionary key and then mutated, dictionary behavior can become incorrect.

---

## 17. `ClassVar`

Use `ClassVar` for class-level values that should not be treated as dataclass fields.

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class User:
    username: str
    role: str
    table_name: ClassVar[str] = "users"
```

`table_name` is not part of the generated constructor.

```python
User("val", "admin")
```

not:

```python
User("val", "admin", "users")
```

---

## 18. Inheritance

Dataclass inheritance works, but field order matters.

```python
@dataclass
class Person:
    name: str

@dataclass
class Student(Person):
    student_id: str
    year: int
```

The generated initializer is roughly:

```python
def __init__(self, name: str, student_id: str, year: int):
    ...
```

Inherited fields come first.

This can fail:

```python
@dataclass
class Base:
    x: int = 0

@dataclass
class Child(Base):
    y: int
```

because `y` is a required field following a default field `x` inherited from the base class.

---

## 19. Conversion and inspection helpers

The `dataclasses` module provides useful helpers:

```python
from dataclasses import asdict, astuple, fields, replace
```

Example:

```python
from dataclasses import dataclass, asdict, astuple, fields, replace

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)

print(asdict(p))
print(astuple(p))
print(replace(p, y=99))
print([f.name for f in fields(p)])
```

Output:

```text
{'x': 1, 'y': 2}
(1, 2)
Point(x=1, y=99)
['x', 'y']
```

These helpers also work with slotted dataclasses.

---

## 20. Python 3.14 note: `make_dataclass(..., decorator=...)`

`make_dataclass()` dynamically creates dataclasses.

```python
from dataclasses import make_dataclass

Point = make_dataclass(
    "Point",
    [("x", int), ("y", int)],
)

p = Point(1, 2)
print(p)
```

Output:

```text
Point(x=1, y=2)
```

In Python 3.14, `make_dataclass` includes a `decorator` parameter. This allows dynamic dataclass creation to use a custom decorator instead of the standard `dataclass` function. The default remains `dataclass`.

Source: Python documentation, `dataclasses.make_dataclass`: <https://docs.python.org/3/library/dataclasses.html#dataclasses.make_dataclass>

---

## 21. Practical recommendations

Use a plain dataclass for ordinary structured data:

```python
@dataclass
class PlaintextDocument:
    abbreviation: str
    year: int
    publisher: str
    text: str
```

Use `slots=True` for compact, fixed-schema records:

```python
@dataclass(slots=True)
class Token:
    text: str
    start: int
    end: int
```

Use `frozen=True, slots=True` for immutable-ish value objects:

```python
@dataclass(frozen=True, slots=True)
class DocumentId:
    collection: str
    number: int
```

Use immutable contained types when you want stronger value-object behavior:

```python
@dataclass(frozen=True, slots=True)
class SearchResult:
    document_id: str
    score: float
    tags: tuple[str, ...]
```

Avoid `slots=True` when:

- you want to attach arbitrary attributes dynamically;
- you rely on `__dict__` directly;
- a framework expects normal mutable instance dictionaries;
- you use ad-hoc cached attributes without declaring them as fields.

Avoid `frozen=True` if:

- the object is naturally mutable;
- fields will be updated repeatedly;
- you store mutable containers and expect full immutability;
- you need ordinary assignment in `__post_init__` and do not want to use `object.__setattr__`.

---

## 22. What dataclasses are good for

Dataclasses are good for:

- internal data-transfer objects;
- configuration objects;
- parsed records;
- algorithm inputs and outputs;
- small domain value objects;
- intermediate structured results;
- test fixtures;
- compact records when combined with `slots=True`.

They are not automatically:

- runtime validators;
- database models;
- JSON serializers;
- ORM entities;
- security boundaries;
- deep immutable objects.

For runtime validation and serialization-heavy workflows, consider additional tools such as Pydantic, attrs, Marshmallow, or custom validation logic.

---

### 23. References

- Python documentation: `dataclasses` module: <https://docs.python.org/3/library/dataclasses.html>
- Python documentation: `dataclasses.dataclass`: <https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass>
- Python documentation: `dataclasses.field`: <https://docs.python.org/3/library/dataclasses.html#dataclasses.field>
- Python documentation: `dataclasses.make_dataclass`: <https://docs.python.org/3/library/dataclasses.html#dataclasses.make_dataclass>
- Python documentation: data model and `__slots__`: <https://docs.python.org/3/reference/datamodel.html#slots>
