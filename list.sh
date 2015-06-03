#!/usr/bin/env bash

export WORKON_HOME=~/Envs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2
source /usr/bin/virtualenvwrapper.sh

workon source-servers-list
`which python2` list.py