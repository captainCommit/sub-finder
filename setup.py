from setuptools import setup, find_packages
from platform import python_version_tuple
import sys, os

version = '0.1'

setup(
    name='subd',
    version=version,
    description="Download Subtitles Easily",
    keywords='Subtitles Python',
    author='Suparno Karmakar',
    author_email='ssuparno1998@gmail.com',
    url='https://twitter.com/1729Suparno',
    license='Apache License, Version 2.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'Support for encoding detection on downloaded subtitle':
            [
                'charset_normalizer' if int(python_version_tuple()[0]) >= 3 else 'chardet'
            ],
    }
)