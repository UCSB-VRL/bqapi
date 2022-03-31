from setuptools import setup, find_packages


setup(
    name='bqapi-ucsb',
    version='1.0.1',
    author="Bisque Team",
    author_email='manj@ucsb.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='API Bisque',
    url='https://github.com/UCSB-VRL/bisqueUCSB',
    install_requires=[
          'six', 'lxml', 'requests==2.10.0', 'requests-toolbelt',
      ],

)
