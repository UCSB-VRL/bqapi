from setuptools import setup, find_packages


# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='bqapi-ucsb',
    version='1.0.2',
    author="Bisque Team",
    author_email='amil@ucsb.edu',
    description="""Python API for interacting with BisQue""",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='API Bisque',
    url='https://github.com/UCSB-VRL/bisqueUCSB',
    install_requires=[
        'six',
        'lxml',
        'requests==2.10.0',
        'requests-toolbelt',
    ],
)
