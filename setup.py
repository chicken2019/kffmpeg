import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kffmpeg",
    version="0.1.1",
    author="Kovacs Kristof-Attila",
    description="kffmpeg",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/kffmpeg",
    packages=setuptools.find_packages(),
    install_requires=["kov_utils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)