#!/bin/bash
# mypy typechecking

set -ex

mypy --ignore-missing-imports sigid
