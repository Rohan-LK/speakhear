import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="speaklisten", # Replace with your own username
    author="ROHAN LAL KSHETRY",
    author_email="rlkshetry95@gmail.com",
    description="speak() to speak out the value, takecommand().lower() to listen to the input",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rohan-LK/speakhear",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
