import setuptools

setuptools.setup(
    name="search-suggestion",
    version="0.1.0",
    author="Chris Oh",
    author_email="chris@5tigerjelly.com",
    description="Search query suggestion service",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/5tigerjelly/search-suggestion-python",
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='search, autosuggestion, suggestion',
    python_requires='>=3.6',
)