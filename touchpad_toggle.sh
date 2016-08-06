#!/bin/sh

id=$(xinput list | grep -Eio 'GlidePoint\s*id\=[0-9]{1,2}' | grep -Eo '[0-9]{1,2}')
enabled=$(xinput list-props $id | grep 'Device Enabled' | awk '{print $4}')

[ $enabled == 1 ] && xinput disable $id || xinput enable $id

# Device ID of TouchPad that registered in X : xinput list | grep -Eio 'GlidePoint\s*id\=[0-9]{1,2}' | grep -Eo '[0-9]{1,2}'
# Status On/Off of Touchpad : xinput list-props $ID | grep 'Device Enabled' | awk '{print $4}
