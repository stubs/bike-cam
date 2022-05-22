#!/bin/bash


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
python "$SCRIPT_DIR"/capture.py --dt $(date -I) --hour $(date "+%H") --min $(date "+%M")
