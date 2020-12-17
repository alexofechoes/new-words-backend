.PHONY: makemigrations
makemigrations:
	docker-compose exec app  python src/manage.py makemigrations

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
