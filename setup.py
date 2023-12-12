try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Christmas Theamed codebar project',
    'author' : 'Roland Rebek',
    'url' : 'https://github.com/Roland87/Codebar-Christmas-theamed',
    'download_url' : 'https://github.com/Roland87/codebar-christmas-project/archive/v0.1.tar.gz',
    'author_email' : 'roland.rebek87@gmail.com',
    'version' : '0.1',
    'install_requires' : ['pytest', 'flask'],
    'packages' : [],
    'scripts' : [],
    'name' : 'Codebar Christmas Project'
}

setup(**config)