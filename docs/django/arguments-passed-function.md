# Arguments passed to a function

Good question — that leading `*` in a Python function signature is a **syntax feature** that changes **how arguments can be passed** to a function.

Let’s look at your example again:

```python
def create_new_wallet(
    *,
    path,
    config: SimpleConfig,
    passphrase: Optional[str] = None,
    password: Optional[str] = None,
    encrypt_file: bool = True,
    seed_type: Optional[str] = None,
    gap_limit: Optional[int] = None,
    gap_limit_for_change: Optional[int] = None,
) -> dict:
```

---

### ✅ What the `*` Means

The single `*` means that **all parameters that come after it must be passed by keyword**, not by position.

So you **must** call the function like this:

```python
create_new_wallet(path="/tmp/test_wallet", config=my_config)
```

and **not** like this:

```python
create_new_wallet("/tmp/test_wallet", my_config)  # ❌ TypeError
```

If you try the positional form, Python raises:

```
TypeError: create_new_wallet() takes 0 positional arguments but 2 were given
```

---

### 🧠 Why Use It

This is called **keyword-only parameters**.
Developers use it for clarity and safety — to make sure it’s obvious which argument is which, especially when a function has many optional parameters.

For example:

```python
def resize_image(*, width, height):
    ...
```

You must call:

```python
resize_image(width=100, height=200)
```

not:

```python
resize_image(100, 200)  # ❌ unclear
```

---

### 🧩 In Context of `create_new_wallet()`

Electrum uses `*` to **force you** to specify important arguments like `path` and `config` by name, so that you don’t accidentally swap them:

✅ Correct:

```python
create_new_wallet(path="/home/al/.electrum/testnet/wallets/send", config=_config)
```

❌ Wrong:

```python
create_new_wallet("/home/al/.electrum/testnet/wallets/send", _config)
```

---

### ✅ Quick Summary

| Symbol      | Meaning                                               |
| ----------- | ----------------------------------------------------- |
| `*args`     | Collects any **positional** arguments into a tuple.   |
| `**kwargs`  | Collects any **keyword** arguments into a dict.       |
| `*` (alone) | Says “all following parameters must be keyword-only.” |

So in `create_new_wallet`, the `*` ensures you always call it with named parameters for clarity and correctness.
