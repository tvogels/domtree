from setuptools import find_packages, setup

setup(
    name="domtree",
    version="0.0.4",
    description="DOM Tree syntax for python",
    url="http://github.com/tvogels/domtree",
    author="Thijs Vogels",
    author_email="t.vogels@me.com",
    license="MIT",
    packages=find_packages(),
    zip_safe=True,
    install_requires=["typing_extensions>=4"],
)
