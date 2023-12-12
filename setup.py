try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Christmas Theamed codebar project',
    'author' : 'Roland Rebek',
    'url' : 'URL to get it at.',
    'download_url' : 'Where t download it.',
    'author_email' : 'roland.rebek87@gmail.com',
    'version' : '0.1',
    'install_requires' : ['pytest', 'flask'],
    'packages' : ['pytest', 'flask'],
    'scripts' : [],
    'name' : 'Codebar Christmas Project'
}

setup(**config)