#!/bin/bash
set -o errexit

find . -name '*.py' \
  | grep -v "venv\|env" \
  | xargs pylint \
  --errors-only \
  --disable=print-statement

echo 'Passes pylint check'
