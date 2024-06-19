# setup.py

from setuptools import setup, find_packages

setup(
    name="nambazasimu",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    test_suite='tests',
    author="Alex Mkwizu",
    author_email="alexgmkwizu@gmail.com",
    description="A package to identify Tanzanian phone number carriers.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/genie360s/nambazasimu",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
