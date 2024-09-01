# Python Shell and play around with the free API Django provides

To start the Python shell, use this command:

```bash
❯ python manage.py shell
```

This will open the Python shell, where you can play around with the free API Django provides. Try this:

```python
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
(output)<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
(output)1

# Access model field values via Python attributes.
>>> q.question_text
(output):"What's new?"
>>> q.pub_date
(output)datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
(output)<QuerySet [<Question: Question object (1)>]>

>>> Exit()
```

After edit the `polls/models.py` file, run again the command `python manage.py shell` and try the following:

```bash
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
# <QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
# <QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
# <QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
#<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#   File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/db/models/query.py", line 649, in get
#     raise self.model.DoesNotExist(
# polls.models.Question.DoesNotExist: Question matching query does not exist.


# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
#<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
# True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set (defined as "choice_set") to hold the "other side" of a ForeignKey
# relation (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
# <QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text="Not much", votes=0)
# <Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
# <Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
# <Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
# <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
# 3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
# <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

## Create an admin user

To create an admin user, use this command:

```bash
❯ python manage.py createsuperuser
```

Enter your desired username and press enter.

```bash
Username: admin # this is an example, you can use any username
```

You will then be prompted for your desired email address:

```bash
Email address: admin@python.org # this is an example, you can use your email
```

The final step is to enter your password. You will be asked to enter your password twice, 
the second time as a confirmation of the first.

```bash
Password: ********
Password (again): ********
Superuser created successfully.
```

## Identify a bug

```bash
python manage.py shell
Python 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True # this is a bug, must be False
```

## The Django test client

Django provides a test Client to simulate a user interacting with the code at the view level. We can use it in tests.py or even in the shell.

We will start again with the shell, where we need to do a couple of things that won’t be necessary in tests.py. The first is to set up the test environment in the shell:

```bash
❯ python manage.py shell
```

Then, we need to import the test Client class:

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```
setup_test_environment() installs a template renderer which will allow us to examine some additional attributes on responses such as response.context that otherwise wouldn’t be available. Note that this method does not set up a test database, so the following will be run against the existing database and the output may differ slightly depending on what questions you already created. You might get unexpected results if your TIME_ZONE in settings.py isn’t correct. If you don’t remember setting it earlier, check it before continuing.

Next we need to import the test client class (later in tests.py we will use the django.test.TestCase class, which comes with its own client, so this won’t be required):

```python
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
```

Now we can use this client to simulate GET and POST requests on our views. For example, we can test the index page:

```python
>>> # get a response from '/'
>>> response = client.get("/")
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
# 200
>>> response.content
# b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
# <QuerySet [<Question: What's up?>]>