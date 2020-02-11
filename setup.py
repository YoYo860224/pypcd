import os
from setuptools import setup, find_packages

# Description should be a one-liner:
description = "Pure Python PCD reader/writer"

# Long description will go up on the pypi page
long_description = """\
pypcd
========

Pure Python reader/writer for the PCL ``pcd`` data format for point clouds.

Please go to the repository README_.

.. _README: https://github.com/dimatura/pypcd/blob/master/README.md

License
=======
``pypcd`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2015--, Daniel Maturana
"""

setup(
    name="pypcd",
    version="1.0",
    author="Daniel Maturana",
    maintainer="Chen Yo-Cheng",
    maintainer_email="m10715094@mail.ntust.edu.tw",
    description=description,
    long_description=long_description,
    url="https://github.com/YoYo860224/pypcd",
    license="MIT",
    platforms="OS Independent",
    packages=find_packages(exclude=('*tests', '*docs')),
    package_data={'pypcd': [os.path.join('test_data', '*')]},
    install_requires=["numpy", "lzf"]
)
