ruff format .
ruff check --fix .
pylint --disable=C,R,W --enable=E --recursive=y .
pytest