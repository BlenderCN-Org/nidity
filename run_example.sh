#!/usr/bin/env sh

set -e

EXAMPLE=${1:-hello_world}

(
    cd $(dirname $0)
    blender \
        -noaudio \
        --background \
        --factory-startup \
        --python examples/example_context.py \
        --python examples/${EXAMPLE}.py \
        ;
)
