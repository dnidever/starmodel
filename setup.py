#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="starmodel",
      version='1.0.0',
      description='Stellar structure model',
      author='David Nidever',
      author_email='dnidever@montana.edu',
      url='https://github.com/dnidever/starmodel',
      packages=find_packages(exclude=["tests"]),
      scripts=['bin/doppler'],
      install_requires=['numpy','astropy(>=4.0)','scipy','dlnpyutils(>=1.0.3)']
)
