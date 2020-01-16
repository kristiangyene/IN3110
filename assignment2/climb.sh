#!/bin/bash
climb() {
    local steps i
    if [ -z "$1" ]
    then
        steps+=../
    else
        for (( i=0; i < $1; i++ )); do
            steps+=../
    done
    fi
    cd "$steps"
}