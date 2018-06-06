import codecs
from setuptools import setup

setup(
    name="dumpls",
    version="3.0.0",
    packages=['dumpls', 'dumpls.crypto'],
    package_data={
        'dumpls': []
    },
    install_requires=[],
    entry_points="""
    [console_scripts]
    dslocal = dumpls.local:main
    dsserver = dumpls.server:main
    """,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
