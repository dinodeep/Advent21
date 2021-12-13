#!/bin/bash

if [ -d $1 ]; then
    echo Directory exists
else 
    echo Constructing directory and files for $1

    mkdir $1
    cd $1
    touch easyinput.txt hardinput.txt part1.py part2.py

    echo Done creating files
fi