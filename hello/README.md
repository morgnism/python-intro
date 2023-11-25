# Python Tutorials: Getting started with VSCode

## Interpreter

Python is an interpreted language meaning that each line is read one-by-one. Each line is turned into a compiled language as the code is read by the interpreter.

The interpreter needs to be selected. This can be done in the following steps:

1. Open the command palette (shift + cmd + p)
2. Type "Python: Select Interpreter" and select that option
3. Then choose the corresponding one for the current version of Python

## Running a file

There a several ways to run a file. VSCode adds a Run/Play bar icon to the top right. You can also add a custom command to run it by the following:

1. Open the command palette
2. Type "Preferences: Open Keyboard Shortcuts"
3. Select the first icon in the top right to open as JSON. This will open the `keybindings.json` file.
4. Add the following to the existing user-defined shortcuts:

```json
{
  "key": "shift+alt+r",
  "command": "python.execInTerminal"
}
```

### Debugging

It's also possible to use VSCode's debugger in the right panel. Just add a breakpoint to a line of a file, then run the debugger. This is similar to a browser's debugging in JavaScript.

## Setup

Ideally, we want to have an app/package that's similar to an npm package and its `node_modules`. For this, we can use `make` with the following file structure where a `requirements` file contains a list of dependencies in key-value parts separated by '=':

```
numpy=1.22.3
```

In a `makefile`, like this simple example:

```makefile
run:
	python3 hello.py

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pychache__
```

However, we can improve the `makefile` by using a dedicated project environment.

### Virtual Environment

Sometimes it isn't ideal to save packages globally which are needed by a few projects. We can also leverage variables in `make`. So we edit the `makefile` like so:

```makefile
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) hello.py

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pychache__
	rm -rf $(VENV)
```
