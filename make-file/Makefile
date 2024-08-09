install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# --nbval is a notebook plugin
	python -m pytest --nbval notebook.ipynb
	
	# verbosity: -v, -vv or quiet -q, -qq
	python -m pytest -vv --cov=app test_app.py

format:
	black *.py

lint:
	# Use --disable=R,C to ignore refactor and convention
	pylint  hello.py

all: install lint test