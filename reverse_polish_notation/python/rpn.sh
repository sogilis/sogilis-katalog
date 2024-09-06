#! /bin/bash

read LINE
echo "32 k $LINE p" | dc | sed -e 's/^\./0./' | sed -e 's/\([^0]\)0*$/\1/'
