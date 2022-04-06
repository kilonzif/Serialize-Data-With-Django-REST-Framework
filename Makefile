run:
	python manage.py runserver

make:
	python manage.py makemigrations api

migrate:
	python manage.py migrate

freeze:
	pip freeze > requirements.txt		

test:
	python manage.py test

drop:
	dropdb api

create:
	createdb api

live:
	python manage.py livereload

activate:
	source virtual/Scripts/activate

set:
	set PGUSER=postgres

admin:
	python manage.py createsuperuser --username admin --email admin@admin.com
