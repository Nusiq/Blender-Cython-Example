# Blender Cython Example
This repository contains a simple example of a Blender addon implemented in
Cython and lists some of the issues that have been encountered during its
development. The addon registers single operator called
"Cython Test: My Operator" which prints a message to console when activated.

## What's Cython?
[Cython](https://cython.readthedocs.io) is a superset of the Python language
which compiles to C. Compiled C code is compatible with the Python interpreter.
The main benefit of cython is its speed. The downside of Cython is that after
compilation it's not platform independent.

## Compilation
### Requirements
- Python with the version that matches the version used by Python shipped
  with Blender. For exmple Blender 3.1 uses Python 3.10 so the files need to
  be compiled with Python 3.10. You can check which version of Python is
  installed on Blender by opening its interactive Python console (SHIFT+F4).
- Cython module installed on Python (`pip install cython`).
- `C` complier installed on the system.

### Compilation
There are two ways to compile the addon, using the `setup.py` script with:
```
python setup.py build_ext --inplace
```
or using the `cythonize` command which should be availabe after installing
Cython.
```
cythonize -i *.pyx
```
The second option doesn't work if the path to the module contains symbols which
aren't allowed in Python modules. For example if this directory were called,
*Blender-Cython-Example*, it wouldn't wrok because of the dashes.
The first method doesn't have that limitation.

Both methods create some `*.c` and `*.pyd` (Windows) or `*.so` (Linux) files.

## Installation
After compilation, the addon that uses Cython is the same as any other addon.
You need to create a zip file with files used by the addon (in this case all
of the *.py and *.pyd files) and install it using Blender's built-in addons
manager.

**WARNING**: The files in the ZIP must be in a subdirectory. Don't put them
directly in the root.

This repository doesn't provide a zip file, as it's only an example and the
addon doesn't do anything useful.s

## Promblems with uninstalling
The Cython modules can't be uninstalled using Blender's addon manageer because
blender fails to remove the *.pyd files, while it's running. In order to
uninstall the addon you have to delete the files manually while Blender is
off.


