from distutils.core import setup
with open('README.md') as f:
    long_description = f.read()
setup(
  name = 'py-data-structure',         # How you named your package folder (MyLib)
  packages = ['py-data-structure'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package that allows you to implement C++ data structures in Python.',
  long_description=long_description,# Give a short description about your library
  long_description_content_type='text/markdown',
  author = 'Vihan',                   # Type in your name
  author_email = 'vihan.raval1@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/tinyCodersDen/py-data-structure',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/tinyCodersDen/py-data-structure/archive/refs/tags/v_0.1.1.tar.gz',    # I explain this later on
  keywords = ['Data','structures','data structures','stacks','queues'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)