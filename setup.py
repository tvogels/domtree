from setuptools import setup, find_packages

setup(
    name="domtree",
    version="0.0.2",
    description="DOM Tree syntax for python",
    url="http://github.com/tvogels/domtree",
    author="Thijs Vogels",
    author_email="t.vogels@me.com",
    license="MIT",
    packages=find_packages(),
    zip_safe=True,
    install_requires=["typing_extensions>=4"],
)
