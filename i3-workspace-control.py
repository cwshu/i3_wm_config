#!/usr/bin/env python3
'''
control i3 workspaces, like move up/down/left/right (2d grid workspace emulation)
i3 control is based on i3-msg program

https://github.com/benkaiser/i3-wm-config/blob/master/workspace_controller.py
http://i3wm.org/docs/ipc.html#_workspaces_reply
'''

import sys
import subprocess as sp
import json

# ws: workspace

def get_current_ws_name():
    '''
    get current workspace name.
    '''
    handle = sp.Popen(['i3-msg', '-t', 'get_workspaces'], stdout=sp.PIPE)
    workspaces = handle.communicate()[0]
    workspaces = json.loads(workspaces.decode())

    workspaces = sorted(workspaces, key=lambda k: k['name'])
    for ws in workspaces:
        if ws['focused']:
            return ws['name']

def goto_ws(ws_num):
    sp.Popen(['i3-msg', 'workspace '+str(ws_num)], stdout=sp.PIPE)

def move_container_to_ws(ws_num):
    sp.Popen(['i3-msg', 'move container to workspace '+str(ws_num)], stdout=sp.PIPE)

WS_COLUMN = 4
direction_to_ws_diff = {
    'left': -1,
    'right': 1,
    'up': -1*WS_COLUMN,
    'down': WS_COLUMN,
}
def goto_ws_direction(direction):
    current_ws = int(get_current_ws_name())
    next_ws = current_ws+direction_to_ws_diff[direction]
    goto_ws(next_ws)
def move_to_ws_direction(direction):
    current_ws = int(get_current_ws_name())
    next_ws = current_ws+direction_to_ws_diff[direction]
    move_container_to_ws(next_ws)

def main():
    if len(sys.argv) != 3:
        sys.exit('{} <go|move> <direction>'.format(sys.argv[0]))

    _type = sys.argv[1]
    direction = sys.argv[2]
    if _type not in ('go', 'move'):
        sys.exit('{} isn\'t correct type'.format(_type))
    if direction not in ('up', 'down', 'left', 'right'):
        sys.exit('{} isn\'t direction'.format(direction))

    if _type == 'go':
        goto_ws_direction(direction)
    elif _type == 'move':
        move_to_ws_direction(direction)
        goto_ws_direction(direction)

if __name__ == '__main__':
    main()
