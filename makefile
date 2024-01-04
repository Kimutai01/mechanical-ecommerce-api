start_services:
	docker compose up -d --force-recreate

stop_services:
	docker compose down
build:
	docker compose up --build -d
migrate:
	docker compose exec mechanic python manage.py migrate

makemigrations:
	docker compose exec mechanic python manage.py makemigrations

django_shell:
	docker compose exec mechanic python manage.py shell

container_shell:
	docker compose run mechanic sh

collectstatic:
	docker compose exec mechanic python manage.py collectstatic

	