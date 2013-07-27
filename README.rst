====================================================
42 Coffee Cups Test Assignment
====================================================

Coffee42Test is examoles of solving assigments of 42 Coffee Cups company.
#57888 PO BOX 105603, Atlanta, GA 30348, USA

.. Contents::
=============


Ticket 1: Personal Data
-----------------------

**Show your name, surname, bio, contacts on the main page**

Create basic django-проект that would present your name, surname, date of birth, bio, contacts on the main page. Data should be stored in the DB, that's

* manage.py syncdb
* manage.py runserver
* open the browser and all data are in, loaded from fixtures

Use pip requirements and virtualenv to manage your third party packages dependencies

Use *south*, you'll need it later

There should be *Makefile* with *test* target running your tests (make test to verify it)

Mockup: http://framebox.org/Awq-bCzXsh

Also, post with first comment this links:

* Project on GetBarista;
* Staging's address;
* Repo on Github.

**Change History**

* Description modified (diff)
* Summary changed from на головній сторінці вивести твої ім'я/фамілію/біо/контакти to show your name, surname, bio, contacts on the main page

# Corresponding branch name:   t1_persona_data


Ticket 2: (Merged to ticket 1)
``````````````````````````````

Ticket 3: Middleware
--------------------

**Create middleware that stores all http requests in the DB**

Also, on a separate page show first 10 http requests that are stored by middleware
Mockup:  http://framebox.org/Awv-QVXKyN

**Change History**

* Summary changed from Зробити middleware що зберігає всі запити в базу to Зробити middleware що зберігає всі http запити в базу
