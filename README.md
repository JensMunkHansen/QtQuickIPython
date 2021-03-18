# QtQuickIPython

This is a simple example showing how the Jupyter IPython interpreter
can be embedded into a modern QtQuick application.

The example is embedding a Jupyter interpreter as an in-process
interpreter, so it is possible to interact with the main application.

The example is embedding the interpreter in a QtQuick Python
application. For a C++ application, the interested user can
re-implement the InterpreterItem.py in C++ and register a `PyObject*`
using PySide2.

To get the example up and running, you need a Qt installation and installing the following in an either virtual Python environment or the system installation of Python

 * PySide2 (5.15.2)
 * qtconsole

A Qt Creator project file for Qt Creator 4.14.1 `main.pyproject` can be found in the root directory.
 