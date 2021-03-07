init:
	python -m pip install --upgrade pip && python -m venv venv && . ./venv/bin/activate

install:
	pip install -r requirements.txt

run:
	export FLASK_APP=main.py && flask run
