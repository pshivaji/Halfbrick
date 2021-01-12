
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="halfsolbrick", 
    version="0.0.1",
    author="Shivaji Parala",
    author_email="s.parala@uqconnect.edu.au",
    description="Convert csv to json, generate sql statements and data summary",
    long_description=long_description,
        long_description_content_type="text/markdown",
    url="https://github.com/pshivaji/Halfbrick",
        classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

    install_requires=["numpy>=1.14.0", "pandas>=0.23.4", "matplotlib>=2.2.2"]
)

