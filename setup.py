from setuptools import find_packages, setup

setup(
    name="bqapi-ucsb",
    version="1.0.7",
    author="Bisque Team",
    author_email="amil@ucsb.edu",
    description="""Python API for interacting with BisQue""",
    packages=find_packages("src"),
    package_dir={"": "src"},
    keywords="API Bisque",
    url="https://github.com/UCSB-VRL/bisqueUCSB",
    install_requires=[
        "six",
        "lxml",
        "requests==2.32.3",
        "requests-toolbelt",
    ],
)
