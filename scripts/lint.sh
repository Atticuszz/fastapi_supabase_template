#!/usr/bin/env bash

set -e
set -x

mypy src/app             # type check
ruff check src/app          # linter
ruff format src/app --check # formatter
