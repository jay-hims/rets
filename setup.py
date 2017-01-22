from setuptools import setup

long_desc = 'Python 3 client for the Real Estate Transaction Standard (RETS) Version 1.7.2'

install_requires = [
    'beautifulsoup4>=4.5.1',
    'flake8>=3.2.1',
    'lxml>=3.6.4',
    'requests>=2.12.3',
    'requests-toolbelt>=0.7.0',
    'udatetime>=0.0.11',
]

tests_requires = install_requires + [
    'pytest>=3.0.5',
]

packages = [
    'rets',
    'rets.client',
    'rets.http',
    'rets.http.parsers',
]

setup(
    name='rets',
    version='0.1.0',
    description='rets',
    long_description=long_desc,
    author='Martin Liu',
    author_email='martin@opendoor.com',
    url='https://github.com/opendoor-labs/rets',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ],
    license='MIT License',
    install_requires=install_requires,
    tests_require=tests_requires,
    packages=packages,
)
