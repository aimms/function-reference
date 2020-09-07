#!/bin/bash
# call with yabr verb : commit or push
# creating the doxygen files and pushing it to the yabr repository

#set current directory here
cd "${0%/*}"

mkdir -p "target/all"
cp _build/latex/AIMMS_func.pdf target/all
buildtool/yabr.sh -release -yabr yabr.xml -toolset all $1

python -u writeVersionAndBranchToDB.py


