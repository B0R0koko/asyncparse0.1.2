from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

long_text = """AsyncParse is a library allowing you to make multiple http requests asynchronously using proxies.
Also module has built-in error handling and headers handling allowing to make more requests without getting ip banned.


AsyncParse 0.1.2 (11.03.2022) - First release (basic functionality added)"""
 
setup(
  name='AsyncParse',
  version='0.1.2',
  description='AsyncParse is a library allowing you to make multiple http requests asynchronously',
  long_description=long_text,
  url='',  
  author='Mironov Mihail',
  author_email='devborokoko@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='webscraping',
  packages=find_packages(),
  install_requires=['requests', 'aiohttp', 'bs4'] 
)