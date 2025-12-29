# Usu the old user

That’s a common setup, and totally fine — it just needs a few small adjustments so your **new Ubuntu user** can fully access, edit, and run the old IntelliJ projects.

Let’s go through it clearly and safely.

---

## ✅ Step 1 — Check where your old projects are

You likely have them under the old user’s home directory, for example:

```
/home/olduser/IdeaProjects/
```

If you log in as your new user (let’s say `al1`), you can verify:

```bash
ls -l /home/olduser/IdeaProjects
```

If you see something like:

```
drwxr-xr-x 5 olduser olduser 4096 Dec 25  btc_payments
```

that means the project belongs to your old user and **your new user doesn’t have write access**.

---

## ✅ Step 2 — Fix permissions

### Option A — Permanently transfer ownership to your new user

If the old user account is no longer needed, this is cleanest:

```bash
sudo chown -R al1:al1 /home/olduser/IdeaProjects
```

That changes all files to belong to your new user.

Then move them if you prefer:

```bash
mv /home/olduser/IdeaProjects /home/al1/
```

Now your projects live at:

```
/home/al1/IdeaProjects/
```

---

### Option B — Keep the old user’s directory but allow access

If you still want to keep the old user account for backup/reference, you can just **grant your new user read/write access**:

```bash
sudo chmod -R 770 /home/olduser/IdeaProjects
sudo usermod -aG olduser al1
```

Then log out and back in so the new group membership applies.

---

## ✅ Step 3 — Reopen projects in IntelliJ

1. Start IntelliJ as your **new user**.

2. Choose **File → Open...**

3. Browse to the project folder (e.g. `/home/al1/IdeaProjects/btc_payments`).

4. IntelliJ might prompt:

   > “This project was created under a different user/home. Trust this project?”
   > → click **Trust Project**.

5. IntelliJ will re-index it and use your new user’s settings (JDKs, venv, etc.).

---

## ✅ Step 4 — Update environment references (if needed)

Some IntelliJ configuration files inside the project (like `.idea/workspace.xml` or `.idea/misc.xml`) might still point to paths under your old username.

For example:

```
/home/olduser/.venv/bin/python
```

You can fix that easily:

### In IntelliJ:

1. Go to **File → Settings → Project → Python Interpreter (or SDK)**.
2. Repoint it to your new virtual environment path (e.g. `/home/al1/IdeaProjects/btc_payments/.venv/bin/python`).

If you’re using Django, also check:
**Run → Edit Configurations → Django server** → update the working directory and interpreter there too.

---

## ✅ Step 5 — Clean IntelliJ caches (optional)

If IntelliJ behaves strangely after moving projects:

```bash
rm -rf ~/.cache/JetBrains/IntelliJ*
rm -rf ~/.config/JetBrains/IntelliJ*
```

Then reopen IntelliJ — it will rebuild indexes cleanly for the new user.

---

## ✅ TL;DR

| Step | What to do                                                |
| ---- | --------------------------------------------------------- |
| 1    | `sudo chown -R al1:al1 /home/olduser/IdeaProjects`        |
| 2    | Move projects to `/home/al1/IdeaProjects/`                |
| 3    | Reopen them in IntelliJ and click “Trust Project”         |
| 4    | Fix interpreter/venv paths in IntelliJ settings           |
| 5    | (Optional) Clear IntelliJ cache if paths are inconsistent |

---

Would you like me to show how to **safely copy only selected projects** (e.g. `btc_payments`) from the old user’s home into your new one while preserving Git history and permissions?
