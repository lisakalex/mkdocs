# Start Django project

Starting a new Django project is a quick process, but it is highly recommended to set it up inside a **virtual
environment** to keep your packages isolated and organized.

Here is the clean, standard workflow to get your Django project up and running from scratch.

---

## Step 1: Set Up Your Project Folder & Virtual Environment

Open your terminal (or Command Prompt/PowerShell) and run the following commands to create a folder for your project and
isolate your dependencies:

```bash
# 1. Create a directory for your work and move into it
mkdir my_web_project
cd my_web_project

# 2. Create a virtual environment named '.venv'
python -m venv .venv

# 3. Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows (Command Prompt):
.venv\Scripts\activate
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

```

*(You'll know it worked because you will see `(.venv)` at the beginning of your terminal prompt line.)*

---

## Step 2: Install Django

With your virtual environment active, install the latest version of Django using `pip`:

```bash
pip install django

```

You can verify the installation by checking the version:

```bash
django-admin --version

```

---

## Step 3: Start the Django Project

To initialize the boilerplate files for your project, run the `startproject` command.

> 💡 **Pro-Tip:** Always add a space and a period (`.`) at the end of this command. This tells Django to install the
> project files directly into your *current* folder, preventing it from creating a redundant, confusing nested folder
> structure.

```bash
django-admin startproject myproject .

```

*(Replace `myproject` with whatever you want to name your core configuration folder.)*

### What just happened?

Django just auto-generated a standard layout for you:

```text
my_web_project/            <-- Your main project root
│
├── myproject/             <-- Core configuration package
│   ├── __init__.py
│   ├── settings.py        <-- Global settings & DB config
│   ├── urls.py            <-- Routing/URL declarations
│   ├── asgi.py            <-- Production server entry (Async)
│   └── wsgi.py            <-- Production server entry (Sync)
│
├── .venv/                 <-- Your isolated Python environment
└── manage.py              <-- The command-line tool to run your project

```

---

## Step 4: Run the Local Development Server

Now, let's verify everything is wired up perfectly. Run Django's built-in lightweight development server:

```bash
python manage.py runserver

```

Open your web browser and navigate to **`[http://127.0.0.1:8000/](http://127.0.0.1:8000/)`**. You should be greeted by
the classic, rocket-launching Django success page!

*(To stop the server at any time, just press `Ctrl + C` in your terminal.)*

---

## Next Step: Creating an App

In Django, "projects" are configurations for the overall website, while "apps" are isolated components that actually do
the work (e.g., a blog, a forum, or a payment system).

To start building features, make sure you are in the directory with `manage.py` and run:

```bash
python manage.py startapp myapp

```
