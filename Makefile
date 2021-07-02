.PHONY: makemigrations
makemigrations:
	docker-compose exec app python src/manage.py makemigrations

.PHONY: migrate
migrate:
	docker-compose exec app python src/manage.py migrate

.PHONY: shell
shell:
	docker-compose exec app python src/manage.py shell

.PHONY: createsuperuser
createsuperuser:
	docker-compose exec app python src/manage.py createsuperuser

.PHONY: process_texts
process_texts:
	docker-compose exec app python src/manage.py process_texts

.PHONY: install
install:
	poetry install

.PHONY: lint
lint:
	poetry run flake8 src tests
	poetry run mypy src

.PHONY: test
test:
	poetry run pytest

.PHONY: fmt
fmt:
	poetry run black
	poetry run isort

requirements.txt: pyproject.toml
requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt
