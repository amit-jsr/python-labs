# Python Labs

# 🐍 Python Revision Plan

> Focus: Core Python skills needed as a junior engineer leveling up.
> NLP/DL topics are tracked separately in the nlp-labs repo.

---

## Week 1 — Python Internals

- [ ] `*args` and `**kwargs`
- [ ] Decorators — `@property`, `@staticmethod`, custom decorators
- [ ] Generators & Iterators — `yield`, `__iter__`, `__next__`
- [ ] Context Managers — `with`, `__enter__`, `__exit__`
- [ ] Dunder methods — `__len__`, `__getitem__`, `__repr__`, `__str__`
- [ ] Closures and scope (LEGB rule)
- [ ] **Memory model** — reference counting, `id()`, mutable vs immutable types, aliasing bugs (`a = b = []`)
- [ ] **GIL (Global Interpreter Lock)** — why threads don't give true parallelism, when to use `multiprocessing` instead
- [ ] **Shallow vs Deep copy** — `copy.copy()` vs `copy.deepcopy()`, the nested list/dict bug
- [ ] **`__slots__`** — memory optimization for classes with many instances
- [ ] **Walrus operator `:=`** — assignment expressions in loops and comprehensions (Python 3.8+)
- [ ] **`global` vs `nonlocal`** — modifying variables from outer scopes, comes up with closures

---

## Week 2 — Data Structures & Standard Library

- [ ] List / dict / set comprehensions
- [ ] `collections` — `Counter`, `defaultdict`, `namedtuple`, `deque`
- [ ] `itertools` — `chain`, `islice`, `groupby`, `product`
- [ ] `functools` — `partial`, `lru_cache`, `reduce`
- [ ] Sorting — `sorted()` with `key=`, `operator.itemgetter`
- [ ] **`zip`, `enumerate`, `map`, `filter`** — functional built-ins, very interview-frequent
- [ ] **String internals** — immutability, `join` vs `+` in loops (performance), f-strings vs `.format()`
- [ ] **Regular Expressions (`re`)** — `re.search`, `re.findall`, `re.sub`, named groups
- [ ] **`datetime` module** — parsing, formatting, `timedelta`, `strftime`/`strptime`
- [ ] **`os` and `sys`** — `os.environ`, `os.path`, `sys.argv` (legacy codebases use these heavily)

---

## Week 3 — OOP

- [ ] Classes, `__init__`, instance vs class variables
- [ ] Inheritance and `super()`
- [ ] Abstract classes (`abc.ABC`, `@abstractmethod`)
- [ ] Dataclasses (`@dataclass`)
- [ ] Magic/dunder methods for operator overloading
- [ ] **`@classmethod` vs `@staticmethod`** — `cls` factory pattern vs utility methods, when to use each
- [ ] **`@property`, `@setter`, `@deleter`** — encapsulation without breaking the interface
- [ ] **`__new__` vs `__init__`** — object creation vs initialization, singleton pattern
- [ ] **MRO (Method Resolution Order)** — `__mro__`, diamond problem, how `super()` resolves in multiple inheritance
- [ ] **Composition vs Inheritance** — when to prefer one over the other (common design interview topic)
- [ ] **`isinstance()` vs `type()`** — subtle difference with inheritance, which to use and why
- [ ] **Mixins** — lightweight reusable behavior without full inheritance chains

---

## Week 4 — File I/O, Serialization & Error Handling

- [ ] Reading/writing `.txt`, `.csv`
- [ ] `pathlib.Path` — modern file path handling
- [ ] Exception handling — `try/except/finally`, custom exceptions
- [ ] `logging` module — replacing `print` with proper logs

### 📄 File Formats
- [ ] **JSON** — `json.load()`, `json.dump()`, `json.dumps()`, nested structures, handling edge cases
- [ ] **Parquet** — columnar format, read/write with `pandas` (`read_parquet`, `to_parquet`), why it's faster than CSV
- [ ] **CSV vs JSON vs Parquet** — know when to use which (size, schema, speed)
- [ ] **pickle** — serialization, security caveats, when NOT to use it

---

## Week 5 — Performance & Tooling

- [ ] Generators vs lists — memory trade-offs
- [ ] `multiprocessing` vs `threading` — when to use which
- [ ] `concurrent.futures` — `ThreadPoolExecutor`, `ProcessPoolExecutor`
- [ ] Profiling — `cProfile`, `timeit`
- [ ] Type hints — `int`, `str`, `list[str]`, `Optional`, `Union`, `TypedDict`
- [ ] **`asyncio`** — `async/await`, event loop basics, `asyncio.gather()` (modern APIs, LLM clients)

---

## Week 6 — Debugging, CLI & Project Structure

### 🐛 Debugging (Interview Hot Topic)
- [ ] `pdb` — `python -m pdb script.py`, setting breakpoints in code
- [ ] `breakpoint()` — built-in shortcut (Python 3.7+)
- [ ] Key `pdb` commands — `n` (next), `s` (step), `c` (continue), `p` (print), `l` (list), `q` (quit)
- [ ] VS Code debugger — launch configs, watch variables, call stack
- [ ] Common debugging patterns — print vs pdb, when to use each

### 🛠️ CLI & Project Structure
- [ ] `argparse` — building CLI tools
- [ ] Virtual environments — `venv`, `pip`, `requirements.txt`
- [ ] Project layout — `src/`, `tests/`, `__init__.py`
- [ ] Writing tests with `pytest` — fixtures, parametrize
- [ ] **`unittest.mock` / `pytest-mock`** — mocking external calls, patching, `MagicMock`

---

## Reference Projects in This Repo

| Project | Concepts to Practice |
|---|---|
| `word2vec/train.py` | Generators, argparse, logging |
| `dwh-labs/` | File I/O, OOP, error handling |
| `resume-ranker/` | OOP, dataclasses, CLI |

---

## Resources

- [Python Docs](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [Fluent Python (book)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
