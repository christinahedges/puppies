from distutils.core import setup
setup(
  name = 'puppies',
  packages = ['puppies'],
  version = '0.1',
  license='MIT',
  description = 'Puppy based classes for python.',
  author = 'Christina Hedges',
  download_url = 'https://github.com/christinahedges/puppies/archive/v0.1.tar.gz',    # I explain this later on
  keywords = ['puppies', 'puppy'],
  install_requires=['numpy', 'pandas', 'IPython'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
