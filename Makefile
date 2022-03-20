isort:
	poetry run isort .

flake:
	poetry run flake8

black:
	poetry run black .

linters: isort black flake

run-dev:
	poetry run uvicorn src.app.app:app --reload --host 0.0.0.0 --port 8080 --log-level info

run:
	docker-compose up --build
