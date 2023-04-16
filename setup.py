# noqa=D100
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyenv_validator",
    version="0.1.1",
    author="OmbuLabs - The Lean Software Boutique LLC",
    author_email="oss@ombulabs.com",
    desciption="Validate environment variables.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/ombulabs/pyenv-validator",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    filename="dist/pyenv_validator-0.1.1-py3-none-any.whl"
)
