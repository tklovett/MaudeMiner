from distutils.core import setup

setup(
    name='Maude',
    version='0.0.0',
    author='Thomas Lovett',
    author_email='tklovett@umich.edu',
    packages=['maude'],
    license='LICENSE.txt',
    description='A tool for analyzing the FDA\'s MAUDE dataset.',
    long_description=open('README.txt').read(),
    install_requires=[
        "beautifulsoup4 == 4.2.1",
        "SQLAlchemy == 0.8.1",
        "numpy == 1.7.1",
        "pyyaml == 3.10",
        "nltk == 2.0.4"
    ]
)
