====================================================
42 Coffee Cups Test Assignment
====================================================

Coffee42Test is examples of solving assigments of 42 Coffee Cups company.
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

Corresponding branch name:   t1_persona_data


Ticket 2: (Merged to ticket 1)
``````````````````````````````


Ticket 3: Middleware
--------------------

**Create middleware that stores all http requests in the DB**

Also, on a separate page show first 10 http requests that are stored by middleware

Mockup:  http://framebox.org/Awv-QVXKyN

**Change History**

* Summary changed from Зробити middleware що зберігає всі http запити в базу to Create middleware that stores all http requests in the DB.

Corresponding branch name:   t3_middleware


Ticket 4: Context Processor
---------------------------

**Create template-context-processor that adds django.settings to the context**

**Change History**

* Summary changed from створити template context processor який додає django.settings в контекст to Create template-context-processor that adds django.settings to the context.

Corresponding branch name:   t4_context_processor


Ticket 5: Form
---------------

**Create page with a form that allows to edit data, presented on the main page**

Create page with a form that allows to edit data, presented on the main page

Add auth to this page.

Upload and show photo.

Upload your photo with a towel to your test server on getBarista.

Mockups:

* http://framebox.org/wsv-tfwFbz
* http://framebox.org/wSk-YPMrdM

**Change History**

* Description modified (diff)
* Summary changed from створити сторінку з формою де можна редагувати дані to Create page with a form that allows to edit data, presented on the main page

Corresponding branch name:   t5_form


Ticket 6: Widget
----------------

**For birth date on the same page add calendar widget**

Create own  `django widget <https://docs.djangoproject.com/en/dev/ref/forms/widgets/>`_

Make this form ajax, using jquery.forms

* submit form via ajax
* indicate loading state
* disable form during submit, so nothing could be entered/changed there

Mockup:  http://framebox.org/AMzD-BTbGcL

**Change History**

* Description modified (diff)
* Summary changed from для дати народження на формі зробити widget календарика to For birth date on the same page add calendar widget.


Ticket 7: (Merged to ticket 6)
``````````````````````````````


Ticket 8: Template Tags
-----------------------

**Create tag that accepts any object and renders the link to its admin edit page**

Create tag that accepts any object and renders the link to its admin edit page ({% edit_link request.user %})

Mockup:  http://framebox.org/AMZF-FNEhjy

**Change History**

* Description modified (diff)
* Summary changed from написати тег що приймає будь-який об'єкт та рендерить посилання на його редагування в адмінці to Create tag that accepts any object and renders the link to its admin edit page.



Ticket 9: Bash Script
---------------------

**Create django command that prints all project models and the count of objects in every model**

Also:

* duplicate output to STDERR with prefix "error: "
* write bash script which execute your command and save output of stderr into file. File name should be current date with extension .dat

**Change History**

* Summary changed from написати django команду що друкує всі моделі проекту і кількість об'єктів в кожній to Create django command that prints all project models and the count of objects in every model.


Ticket 9: Signal Processor
--------------------------

**Create signal processor that, for every model, creates the db entry about the object creation/editing/deletion**

**Change History**

* Summary changed from написати обробник сигналу, який для кожної моделі створює запис в базі про її створення/редагування/видалення to Create signal processor that, for every model, creates the db entry about the object creation/editing/deletion.


Ticket 10: (Merged)
-------------------


Ticket 11: (Merged)
-------------------


Ticket 12: (Merged)
-------------------


Ticket 13: Log Priority
-----------------------

**Your customer sends the change request. Task: understand what he needs and implement.**

Customer's text::

	About requests log: we have to add a priortiy field,
	so we can show the different requests in the order we want.
	Priority 1 (or = 0) will be the standard selection.

Task: understand what he needs and implement.

**Change History**

* Description modified (diff)
* Summary changed from understanding - уявний замовник присилає запит на зміни. Завдання: зрозуміти, що він хоче бачити у результаті і реалізувати. to Your customer sends the change request. Task: understand what he needs and implement.
