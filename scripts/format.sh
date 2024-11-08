#!/bin/sh -e
set -x

ruff check src/app scripts tests --fix
ruff format src/app scripts tests
