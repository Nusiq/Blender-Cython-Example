'''
This script is used to build the Cython modules (the .pyx files). You can run
with:
    python setup.py build_ext --inplace

Alternatively you can use the cythonize tool:
    cythonize -i *.pyx


Both approaches should create some .c and .pyd (Windows) or.so (Linux) files
for each .pyx file. For deployment only the .pyd/.so files are needed.
The first method is better because it works in paths that aren't valid module
names. For exmple, if this directory is named Cython-Test, using 'cythonize'
wouldn't work because the directory has a dash in it.
'''
from setuptools import setup, Extension
from Cython.Build import cythonize

from pathlib import Path
# Passing "*.pyx" unfortunately wouldn't work so we have to specify every
# extension individually in ext_modules.
# https://stackoverflow.com/questions/71983019/why-does-adding-an-init-py-change-cython-build-ext-inplace-behavior

ext_modules = [
    Extension(p.with_suffix("").as_posix(), [p.as_posix()])
    for p in Path(".").rglob("*.pyx")
]

setup(
    ext_modules=cythonize(ext_modules)
)