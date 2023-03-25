from setuptools import find_packages, setup

setup(
  name='termtools',
  version='0.0.4',
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
    'tabulate',
  ],
  entry_points={
    'console_scripts': [
      'bconv = termtools.cli:bconv',
      'hconv = termtools.cli:hconv',
      'dconv = termtools.cli:dconv',
    ]
  }
)