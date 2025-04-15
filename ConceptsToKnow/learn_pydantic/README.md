# learn - pydantic with uv

- Pydantic's primary role is data validation and settings management using Python type hints. It enforces that the data your application receives (from APIs, user input, databases, configuration files, etc.) matches the structure and types you expect.

- pydantic official [docs](https://docs.pydantic.dev/latest/)

  - Pydantic is the most widely used data validation library for Python.
  - with Pydantic, schema validation and serialization are controlled by type annotations.
  - Pydantic models can emit JSON Schema, allowing for easy integration with other tools.
  - Pydantic supports validation of many standard library types including dataclass and TypedDict.

- [Type hints](https://docs.python.org/3/glossary.html#term-type-hint) powering schema validation.An [annotation](https://docs.python.org/3/glossary.html#term-annotation) that specifies the expected type for a variable, a class attribute, or a function parameter or return value.

  - Annotated: Add context-specific metadata to a type.
  - Literal: Special typing form to define literal types (a.k.a. value types).

- The `pyproject.toml` contains metadata about your project.You'll use this file to specify dependencies, as well as details about the project such as its description or license. You can edit this file manually, or use commands like `uv add` and `uv remove` to manage your project from the terminal

```bash
#  to run files
$ uv run main.py
Hello from learn-pydantic!
# to activate environment
uv sync
source .venv\Scripts\activate
$ which python
/c/Users/$$$$$$/Desktop/PythonDev/LearnPython/UnderstandPython/ConceptsToKnow/learn_pydantic/.venv/Scripts/python
# to add any dependency for ex: pydantic
$ uv add pydantic
Resolved 6 packages in 159ms
Installed 5 packages in 96ms
 + annotated-types==0.7.0
 + pydantic==2.11.3
 + pydantic-core==2.33.1
 + typing-extensions==4.13.2
 + typing-inspection==0.4.0

$ uv remove pydantic
Resolved 1 package in 9ms
Uninstalled 5 packages in 73ms
 - annotated-types==0.7.0
 - pydantic==2.11.3
 - pydantic-core==2.33.1
 - typing-extensions==4.13.2
 - typing-inspection==0.4.0
```

## Serialization

Pydantic provides functionality to serialize model in three ways:

- To a Python dict made up of the associated Python objects.
- To a Python dict made up only of "jsonable" types.
- To a JSON string.

## JSON Schema¶

A JSON Schema can be generated for any Pydantic schema

- allowing self-documenting APIs and integration with a wide variety of tools which support the JSON Schema format.

### Notes

- LLMs need to be backwards compatible with existing software.
- validation
- error handling 
- re-ask separate systems
- structured prompts
- structured outputs
- structured thoughts
