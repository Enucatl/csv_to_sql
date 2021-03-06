import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv_to_sql",
    version="0.0.1",
    author="Enucatl",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Enucatl/csv_to_sql",
    project_urls={
        "Bug Tracker": "https://github.com/Enucatl/csv_to_sql/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "pandas >= 1.1",
        "click >= 7.1",
    ],
)
