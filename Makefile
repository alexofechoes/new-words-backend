.PHONY: server makemigrations migrate shell

server:
	poetry run python src/manage.py runserver

makemigrations:
	poetry run src/manage.py makemigrations

migrate:
	poetry run src/manage.py migrate

shell:
	poetry run src/manage.py shell

processed_texts:
	poetry run ./src/process_worker.py
