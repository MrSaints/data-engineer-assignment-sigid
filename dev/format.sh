#!/bin/bash
# Sort imports, remove unused imports, and formats code.

set -ex

isort -rc sigid

autoflake -r --in-place --remove-unused-variables sigid

black sigid
