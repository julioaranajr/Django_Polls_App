# Django_Polls_App

![Django_Polls_App](https://socialify.git.ci/julioaranajr/Django_Polls_App/image?font=Raleway&language=1&name=1&owner=1&pattern=Brick%20Wall&stargazers=1&theme=Dark)

A simple Django application to create and manage polls.

Let’s learn by example.

Throughout this tutorial, we’ll walk you through the creation of a basic poll application.

It’ll consist of two parts:

    A public site that lets people view polls and vote in them.
    An admin site that lets you add, change, and delete polls.

We’ll assume you have Django installed already. You can tell Django is installed and which version by running the following command in a shell prompt (indicated by the $ prefix):

```bash
python -m django --version
```

This tutorial is written for Django 5.0, which supports Python 3.10 and later.

If you don’t have Python installed, you can download it from python.org.

## Creating a project

If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options, and application-specific settings.

From the command line, cd into a directory where you’d like to store your code, then run the following command:

```bash
django-admin startproject mysite
```

This will create a mysite directory in your current directory. If it didn’t work, see Problems running django-admin.

Note:
> You’ll need to avoid naming projects after built-in Python or Django components. In particular, this means you should avoid using names like django (which will conflict with Django itself) or test (which conflicts with a built-in Python package).

Let’s look at what startproject created:

```bash
mysite
├── manage.py
└── mysite
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

These files are:

- The outer **mysite/** root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

- **manage.py**: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about **manage.py** in [django-admin and manage.py](https://docs.djangoproject.com/en/5.0/ref/django-admin/).

- The inner **mysite/** directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. **mysite.urls**).

- **mysite/__ init __.py**: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.

- **mysite/settings.py**: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/5.0/topics/settings/) will tell you all about how settings work.

- **mysite/urls.py**: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/).

- **mysite/asgi.py**: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/) for more details.

- mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/) for more details.

## The development server

Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:

```bash
cd mysite
python manage.py runserver
```

You’ll see the following output on the command line:

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 01, 2024 - 09:38:07
Django version 5.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Note:

> Ignore the warning about unapplied migrations for now; we’ll deal with the database shortly.

You’ve started the Django development server, a lightweight Web server written purely in Python. We’ve included the **runserver** command with the **manage.py** utility.

Note:
> By default, the runserver command starts the development server on the internal IP at port 8000.

Now that the server’s running, visit [http://127.0.0.1:8000/] with your Web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!

## Creating the Polls app

Now that your environment – a “project” – is set up, you’re set to start doing work.

Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

### Projects vs. apps

>What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records, a small poll app, etc. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

Your apps can live anywhere on your Python path. In this tutorial, we’ll create our poll app right next to your manage.py file so that it can be imported as its own top-level module, rather than a submodule of mysite.

To create your app, make sure you’re in the same directory as manage.py and type this command:

```bash
python manage.py startapp polls
```

That’ll create a directory **polls**, which is laid out like this:

```bash
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

This directory structure will house the poll application.

## About me

<a href="https://github.com/julioaranajr/python-course/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=julioaranajr/python-course" alt="Contributors">
</a>

[![GitHub][GitHub-shield]][GitHub-url]
[![Website][website-shield]][website-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

## Contact

Julio Arana Jr. contact me on [https://julioaranajr.com][website-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[GitHub-shield]: https://img.shields.io/badge/-GitHub-black.svg?style=for-the-badge&logo=github&colorB=555
[GitHub-url]: https://github.com/julioaranajr
[website-shield]: https://img.shields.io/badge/-Website-black.svg?style=for-the-badge&logo=github&colorB=555
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/julioarana
[website-url]: https://julioaranajr.com
