#!/usr/bin/env python3

import subprocess as sp
import os

config_dir = os.path.dirname(os.path.abspath(__file__))
home_dir = os.environ['HOME']

print('mkdir -p {}/.config/i3/'.format(home_dir))
print('ln -s {}/i3config {}/.config/i3/config'.format(config_dir, home_dir))
print('mkdir -p {}/.config/i3status/'.format(home_dir))
print('ln -s {}/i3status.conf {}/.config/i3status/config'.format(config_dir, home_dir))
