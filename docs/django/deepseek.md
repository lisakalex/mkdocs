Here's how to set up Aider and integrate it with IntelliJ for your Python development.

---

Step 1: Install Aider

Open a terminal and run:

```bash
python -m pip install aider-install
aider-install
```

That's it. The installer uses uv to create an isolated environment with Python 3.12 and all dependencies .

Alternative one-liner (even if Python isn't installed):

```bash
curl -LsSf https://aider.chat/install.sh | sh
```

Verify the installation:

```bash
aider --version
```

Step 2: Configure API Access

You'll need an API key from an LLM provider. Aider works best with Claude 3.5 Sonnet, GPT-4o, or DeepSeek .

Set your API key as an environment variable:

macOS / Linux:

```bash
export ANTHROPIC_API_KEY=your-key-here
```

Windows PowerShell:

```powershell
setx ANTHROPIC_API_KEY your-key-here
```

To make this permanent on macOS/Linux, add the export line to ~/.zshrc or ~/.bash_profile .

Step 3: Launch Aider in Your Project

Navigate to your Python project and start Aider:

```bash
cd /path/to/your/python-project
aider
```

Or launch with a specific model:

```bash
aider --sonnet     # Claude 3.5 Sonnet
aider --4o         # GPT-4o
aider --deepseek   # DeepSeek
```

Once running, you can ask Aider to:

· "Add error handling to this function"
· "Write unit tests for module.py"
· "Refactor this class to be more modular"

Step 4: Install the IntelliJ Plugin

The Coding-Aider plugin connects IntelliJ directly to Aider .

1. Install the plugin:
   · Go to Settings → Plugins → Marketplace
   · Search for "Coding-Aider"
   · Install and restart IntelliJ
2. Configure API keys in the plugin (optional):
   · Settings → Tools → Aider Settings
   · Add your providers (OpenAI, Anthropic, etc.)
3. Test Aider connection:
   · In Aider Settings, click "Test Aider installation"
   · The plugin can run Aider locally or via Docker 

Step 5: Use Aider from IntelliJ

Once configured, you can use these shortcuts:

Action Shortcut
Start Aider action on selected file(s) Alt + A
Manage persistent files (always in context) Alt + Shift + A
Quick access to all Aider actions Alt + Shift + Q
Auto-commit changes with AI-generated message Alt + D

Workflow example:

1. Right-click a Python file in the project view
2. Select "Start Aider Action" (or press Alt + A)
3. Type your request: "Add docstrings to all functions"
4. Review Aider's changes—they're auto-committed with meaningful messages

The plugin also offers specialized actions:

· Fix Compile Error – let Aider diagnose and fix build/test failures
· Document Code – generate markdown documentation for selected files
· Refactor to Clean Code – apply clean code principles 

Quick Start Summary

```bash
# 1. Install Aider
python -m pip install aider-install && aider-install

# 2. Set API key
export ANTHROPIC_API_KEY=your-key

# 3. Run in your project
cd my-python-project
aider
```

Then install the Coding-Aider plugin in IntelliJ, and you're ready to go.

---

Would you like me to walk through a specific example, like using Aider to write pytest cases for a Python function or refactor a class?