from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.1.'
DESCRIPTION = 'Package to read all data file'
LONG_DESCRIPTION = 'can read all data files with different fill formats'

# Setting up
setup(
    name="Readfiles",
    version="1.0.0",
    author="Punay Mehra",
    author_email="punay.mehra@gmail.com",
    description="This package can read data files with diffrent file formmats",
    packages=["Readallfiles"],
    install_requires=["easygui","pandas","re"],
    keywords=['python', 'Readfiles', 'Read', '.csv', '.xlsx', '.text'],
    classifiers=[
        
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
