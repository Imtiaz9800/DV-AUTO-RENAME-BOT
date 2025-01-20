ruff format .
ruff check --unsafe-fixes --fix --ignore E722,F821 .
pylint --disable=C,R,W,E0401,E0611,E1101,E0213,E1133,E1136,F0401 --enable=E --recursive=y .