MANAGE=django-admin.py

install:
	PYTHONPATH=`pwd` pip install -r requirements.txt --use-mirrors

upgrade:
	PYTHONPATH=`pwd` pip install --upgrade -r requirements.txt --use-mirrors

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=coffe42cups.settings $(MANAGE) test chamber

collectstatic:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=coffe42cups.settings $(MANAGE) collectstatic --noinput

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=coffe42cups.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=coffe42cups.settings $(MANAGE) syncdb --noinput --migrate
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=coffe42cups.settings $(MANAGE) loaddata apps/chamber/fixtures/sir.json
