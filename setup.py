from setuptools import setup
with open('README.md') as f:
    long_description = f.read()
setup(
  name = 'py-data-structure',
  packages = ['py_data_structure'],
  version = '0.1.3',
  license='MIT',  
  description = 'A package that allows you to implement C++ data structures in Python.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Vihan',
  author_email = 'vihan.raval1@gmail.com',
  url = 'https://github.com/tinyCodersDen/py-data-structure',
  download_url = 'https://github.com/tinyCodersDen/py-data-structure/archive/refs/tags/v_0.1.3.tar.gz',
  keywords = ['Data','structures','data structures','stacks','queues'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License'
  ],
)