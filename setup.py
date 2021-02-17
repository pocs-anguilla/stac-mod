import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="STAC-mod",
    version="0.0.1",
    description="A patched version of STAC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["api", "docker", "web"]),
    python_requires='>=3.6',
)
