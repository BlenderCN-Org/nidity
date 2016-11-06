#!/usr/bin/env sh

set -e

(
    cd $(dirname $0)
    blender \
        --background \
        --factory-startup \
        --python examples/hello_world.py
)
