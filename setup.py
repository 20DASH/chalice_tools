from setuptools import setup, find_packages

setup(
    name="chalice_tools",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "chalice"
    ],
    description="Helper tools for development in chalice",
    author="Tito Guidotti",
    author_email="tito.guidotti@gmail.com",
    url="https://github.com/20DASH/chalice-tools"
)