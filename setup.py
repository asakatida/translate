from os import path
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    README = f.read()

setup(
    name='grandquista-translate',
    version='1.0.0',

    author_email='grandquista@gmail.com',
    author='Adam Grandquist',
    description=''.join(README.splitlines()[:4]),
    extras_require={
        'testing': ['pytest'],
    },
    long_description=README,
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    url='https://github.com/grandquista/translate',
)
