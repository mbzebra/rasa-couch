from setuptools import setup, find_packages
import io
import os

install_requires = [
    "rasa==1.0.9"
]

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="rasa-couch",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    version="1.1",
    install_requires=install_requires,
    description="Rasa Couch Tracker Store",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mariswaran",
    author_email="mbzebradev@gmail.com",
    license="GNU General Public License v3.0",
    url="https://github.com/mbzebra/rasa-couch",
    project_urls={
        "Source": "https://github.com/rasahq/rasa-couch"
    },
)
