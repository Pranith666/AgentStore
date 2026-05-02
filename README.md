# AgentStore

Generic Agent Builder project using Streamlit, LangChain, and `uv` for Python
dependency management.

## First-Time Setup

After pulling the repo, install `uv` if you do not already have it:

PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Bash:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart the terminal after installing `uv`, then confirm the install:

```powershell
uv --version
```

If PowerShell does not recognize `uv`, close all terminal windows and open a new
PowerShell window.

## Install Project Dependencies

From the project root:

PowerShell:

```powershell
uv sync
```

Bash:

```bash
uv sync
```

This reads `pyproject.toml` and `uv.lock`, creates the local `.venv/` if needed,
and installs the pinned dependencies.

## Run the Streamlit App

Use `uv run` so commands run inside the project environment:

PowerShell:

```powershell
uv run streamlit run ui/app.py
```

Bash:

```bash
uv run streamlit run ui/app.py
```

Streamlit will print a local URL, usually:

```text
http://localhost:8501
```

## PowerShell Quick Start

For someone who just pulled the repo on Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
uv sync
uv run streamlit run ui/app.py
```

## Adding Dependencies

Use `uv add` instead of manually editing dependency files:

```bash
uv add package-name
```

This updates both `pyproject.toml` and `uv.lock`.

## Useful Commands

```bash
uv sync
uv run streamlit run ui/app.py
uv run python main.py
uv add package-name
uv remove package-name
```

## Git Notes

Do not commit local virtual environments or secrets. The repo ignores:

```text
.venv/
venv/
env/
.env
.env.*
.streamlit/secrets.toml
__pycache__/
```
