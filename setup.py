from setuptools import find_packages, setup

setup(
  name='termtools',
  version='0.0.1',
  description='Terminal Tools',
  author='Natanael',
  author_email='mail@natanael.net',
  packages=find_packages(),
  include_package_data=True,
  package_data={
    'termtools': []
  },
  install_requires=[
    'wheel',
  ],
  entry_points={
    'console_scripts': [
      'b2h = termtools.cli:b2h',
      'h2b = termtools.cli:h2b',
      'b2d = termtools.cli:b2d',
      'd2b = termtools.cli:d2b',
      'bconv = termtools.cli:bconv',
      'hconv = termtools.cli:hconv',
      'dconv = termtools.cli:dconv',
    ]
  }
)