#!/bin/sh -e
set -x

ruff check src/app scripts --fix
ruff format src/app scripts
