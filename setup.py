#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools.command.test import test as TestCommand
import hl7 as _hl7

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run(self):
        import pytest
        pytest.main(self.test_args)
setup(
    name = 'hl7',
    version = _hl7.__version__,
    description = 'Python library parsing HL7 v2.x messages',
    long_description = _hl7.__doc__,
    author = _hl7.__author__,
    author_email = _hl7.__email__,
    url = _hl7.__url__,
    license = _hl7.__license__,
    platforms = ['POSIX', 'Windows'],
    keywords = ['HL7', 'Health Level 7', 'healthcare', 'health care', 'medical record'],
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Communications',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = ['hl7'],
    tests_require = ['pytest'],
    cmdclass = {'test': PyTest},
    zip_safe=True,
)
