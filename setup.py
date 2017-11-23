from setuptools import setup

setup(
  name = 'pyStatus',
  packages = ['pyStatus'],
  version = '0.1',
  description = 'Status bar tool to use with i3bar',
  author = 'Felix Breidenstein',
  author_email = 'pypi@felixbreidenstein.de',
  url = 'https://github.com/f-breidenstein/pyStatus',
  download_url = 'https://github.com/f-breidenstein/pyStatus/archive/v0.1.tar.gz',
  keywords = ['i3wm', 'i3bar'],
  install_requires=['psutil', 'python-musicpd', 'netifaces', 'basiciw'],
  entry_points={
    'console_scripts': {
        'pystatus = pyStatus.runner:main'
    }
  }
)
