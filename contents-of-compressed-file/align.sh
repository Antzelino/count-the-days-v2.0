#!/bin/bash


if [[ $1 < 10 ]]
	then echo "\${alignc 10}"$1
	else echo "\${alignc}"$1
fi

exit 0
