import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robot_and_board", # Replace with your own username
    version="0.0.1",
    author="Wajeeh Ul Hassan",
    author_email="wajeehulhassan_vii@hotmail.com",
    description="A small app for robot and board",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wajeehulhassanvii/robot_and_board",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)