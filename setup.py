import sys

try:
    from skbuild import setup
except ImportError as err:
    msg = (
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself"
    )

    if sys.version_info < (3, 11):
        print(msg, file=sys.stderr)
    else:
        err.add_note(msg)
    raise

from setuptools import find_packages

setup(
    name="domtree",
    version="0.0.4",
    description="DOM Tree syntax for python",
    author="Thijs Vogels",
    author_email="t.vogels@me.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
