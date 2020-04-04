import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ESRNN",
    version="0.0.1",
    author="Kin Gutierrez, Cristian Challu",
    author_email="kin.gtz.olivares@gmail.com, cristianichallu@gmail.com",
    description="Pytorch implementation of the ESRNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kdgutier/esrnn_torch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
