init:
	python3 -m venv venv && . ./venv/bin/activate

install:
	pip install -r requirements.txt

run:
	export FLASK_APP=main.py && flask run
