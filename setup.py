from setuptools import setup, find_packages

setup(
    name="textcleaner",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Add dependencies if needed
    python_requires=">=3.6",
)

setup(
    ...,
    entry_points={
        "console_scripts": ["textcleaner=textcleaner.cleaner:clean_cli"]
    },
)