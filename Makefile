all:
	python manage.py makemigrations contact_info
	python manage.py migrate
	python manage.py loaddata initial_data.json
	python manage.py runserver
