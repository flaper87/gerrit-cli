import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="gerrit-cli",
    version='0.0.1',
    author="Flavio Percoco",
    author_email="flaper87@flaper87.org",
    description=("Gerrit CLI Tool"),
    url="https://github.com/FlaPer87/gerrit-cli",
    packages=find_packages('.'),
    package_data={'': ['LICENSE', 'README.md']},
    include_package_data=True,
    long_description=read('README.md'),
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
    ],
    scripts=[],
    platforms=['Any'],
    install_requires=['distribute', 'cliff', 'python-gerrit'],
    entry_points={
        'gerrit.cli': [
            'reviews list = gerrit_cli.cmd.list:List',
        ],
        "console_scripts": [
            'gerrit = gerrit_cli.cmd.main:main',
        ]
    },
)
