from setuptools import setup

config = {
    'description': 'Pileup',
    'author': 'B. Arman Aksoy',
    'url': 'https://github.com/armish/pileup',
    'download_url': 'https://github.com/armish/pileup/releases',
    'author_email': 'arman@aksoy.org',
    'license': 'http://www.apache.org/licenses/LICENSE-2.0.html',
    'version': '0.0.1',
    'install_requires': [
        'nose>=1.3.7',
        'urwid>=1.3.1',
        'twobitreader>=3.1.0',
        'pysam>=0.8.3'],
    'packages': ['pileup'],
    'scripts': [],
    'name': 'pileup'
}

setup(**config)
