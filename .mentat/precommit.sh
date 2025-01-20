ruff format .
ruff check --unsafe-fixes --fix .
pylint --disable=C,R,W,E0401,E0611,E1101,E0213,E1133,E1136 --enable=E --recursive=y .
pytest