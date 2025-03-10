from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chalice_tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "chalice"
    ],
    description="Helper tools for development in chalice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tito Guidotti",
    author_email="tito.guidotti@gmail.com",
    url="https://github.com/20DASH/chalice_tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)