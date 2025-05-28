try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="flipper",
    version="0.1.0",
    description="Object flipping system for use in RPG bots",
    author="Louis Grenzebach",
    author_email="louis.grenzebach@gmail.com",
    url="https://github.com/pknull/rpg-flip",
    packages=["flipper"],
    package_dir={"flipper": "flipper"},
    include_package_data=True,
    zip_safe=False,
    keywords="rpg flipper",
)
