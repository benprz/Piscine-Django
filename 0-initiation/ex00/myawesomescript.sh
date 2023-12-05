#!/usr/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 bit.ly/link"
    exit 1
fi

link="$1"
content=`curl $1 -s`

echo $content | cut -d '"' -f 2
