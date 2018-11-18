from setuptools import find_packages
from distutils.core import setup
import os
import io


def readfile(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    contents = io.open(path, encoding='utf8').read()
    return contents


setup(
    name="pyexphys",
    version='2.1.2',
    description='Python framework for health/fitness calculations',
    long_description=readfile('README.md'),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    author=u'Doug Fenstermacher',
    author_email='douglas.fenstermacher@gmail.com',
    url='https://dpfens.github.io/PyExPhys',
    keywords='health, physical fitness, cardio, heart rate, VO2Max, energy expenditure, resting metabolic rate, respiration, residual volume, body composition, metabolic equivalents, body surface area, strength, 1-rm, jack daniels',
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ]
)
