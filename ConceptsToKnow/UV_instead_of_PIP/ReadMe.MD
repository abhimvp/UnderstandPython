# UV

- [uv docs](https://docs.astral.sh/uv/) - An extremely fast Python package and project manager, written in Rust.A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and [more](https://docs.astral.sh/uv/#highlights).

```bash
-- ON CMD
C:\Users\******>pipx install uv
  installed package uv 0.6.14, installed using Python 3.11.9
  These apps are now globally available
    - uv.exe
    - uvx.exe
done! ✨ 🌟 ✨

C:\Users\********>uv --version
uv 0.6.14 (a4cec56dc 2025-04-09)

-- ON VSCODE BASH
$ uv
An extremely fast Python package manager.

Usage: uv.exe [OPTIONS] <COMMAND>

Commands:
  run      Run a command or script
  init     Create a new project
  add      Add dependencies to the project
  remove   Remove dependencies from the project
  sync     Update the project's environment
  lock     Update the project's lockfile
  export   Export the project's lockfile to an alternate format
  tree     Display the project's dependency tree
  tool     Run and install commands provided by Python packages
  python   Manage Python versions and installations
  pip      Manage Python packages with a pip-compatible interface
  venv     Create a virtual environment
  build    Build Python packages into source distributions and wheels
  publish  Upload distributions to an index
  cache    Manage uv's cache
  self     Manage the uv executable
  version  Display uv's version
  help     Display documentation for a command

  ...
  ..
  .

```

- uv works with python 3.7 and above.
- **`uv python list`** - gives us the list of python versions above 3.7 on our system and their paths.
- **`uv python install 3.8`** - we can install the specific version we want
- **`uv python find 3.12`** - gives us the installed python version path in our system
  `C:\Users\******\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe`
- $ `uv run main.py` - 3.11.9 (tags/v3.11.9:de54cf5, Apr 2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)]

```bash
$ uv add --script main.py "rich"
Updated `main.py`
# updates the main.py to use rich dependency when running this file
$ uv run main.py
Installed 4 packages in 190ms
3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]
```

- uv for projects (mkdir uvdemoproject)

```bash
... UV_instead_of_PIP/uvdemoproject (main)
$ uv init
Initialized project `uvdemoproject`
```

- gives us some files , and pyproject.toml is similar to requirements.txt file
- uv.lock is similar to package-lock.json - should be used in source control.
