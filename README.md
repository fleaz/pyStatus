# pyStatus

Python tool to use with i3bar

**Needs a proper rewrite...
See https://github.com/f-breidenstein/pyStatus/issues/11 for infos**




## Requirements
* psutil
* python-musicpd
* netifaces
* basiciw

### Install requirements
#### with pip:
* `pip install -r requirements.txt`

## Installation
1) Copy example_runner.py to your runner.py file
    * cp example_runner.py runner.py
2) Edit status_command i3 config in ~/.config/i3/config
    * e.g: status_command ~/workspace/python/pyStatus/runner.py"
3) Make your own configuration in runner.py
