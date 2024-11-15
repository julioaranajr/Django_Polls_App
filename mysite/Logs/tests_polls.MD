# Tests for the Polls App

```bash
python3 manage.py test polls
Found 8 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.EEEEEE.
======================================================================
ERROR: test_past_question (polls.tests.QuestionDetailViewTests)
# The detail view of a question with a pub_date in the past
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Django_Polls_App/mysite/polls/tests.py", line 121, in test_past_question
    response = self.client.get(url)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1129, in get
    response = super().get(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 479, in get
    return self.generic(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 676, in generic
    return self.request(**r)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1092, in request
    self.check_exception(response)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 805, in check_exception
    raise exc_value
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/base.py", line 220, in _get_response
    response = response.render()
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/template/response.py", line 114, in render
    self.content = self.rendered_content
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/template/response.py", line 90, in rendered_content
    template = self.resolve_template(self.template_name)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/template/response.py", line 72, in resolve_template
    return select_template(template, using=self.using)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/template/loader.py", line 47, in select_template
    raise TemplateDoesNotExist(", ".join(template_name_list), chain=chain)
django.template.exceptions.TemplateDoesNotExist: polls/question_detail.html

======================================================================
ERROR: test_future_question (polls.tests.QuestionIndexViewTests)
# Questions with a pub_date in the future aren't displayed on
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Django_Polls_App/mysite/polls/tests.py", line 74, in test_future_question
    response = self.client.get(reverse("polls:index"))
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1129, in get
    response = super().get(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 479, in get
    return self.generic(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 676, in generic
    return self.request(**r)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1092, in request
    self.check_exception(response)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 805, in check_exception
    raise exc_value
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 104, in view
    return self.dispatch(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 143, in dispatch
    return handler(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 154, in get
    self.object_list = self.get_queryset()
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 36, in get_queryset
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: IndexView is missing a QuerySet. Define IndexView.model, IndexView.queryset, or override IndexView.get_queryset().

======================================================================
ERROR: test_future_question_and_past_question (polls.tests.QuestionIndexViewTests)
# Even if both past and future questions exist, only past questions
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Django_Polls_App/mysite/polls/tests.py", line 85, in test_future_question_and_past_question
    response = self.client.get(reverse("polls:index"))
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1129, in get
    response = super().get(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 479, in get
    return self.generic(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 676, in generic
    return self.request(**r)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1092, in request
    self.check_exception(response)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 805, in check_exception
    raise exc_value
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 104, in view
    return self.dispatch(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 143, in dispatch
    return handler(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 154, in get
    self.object_list = self.get_queryset()
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 36, in get_queryset
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: IndexView is missing a QuerySet. Define IndexView.model, IndexView.queryset, or override IndexView.get_queryset().

======================================================================
ERROR: test_no_questions (polls.tests.QuestionIndexViewTests)
# If no questions exist, an appropriate message is displayed.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Django_Polls_App/mysite/polls/tests.py", line 51, in test_no_questions
    response = self.client.get(reverse("polls:index"))
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1129, in get
    response = super().get(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 479, in get
    return self.generic(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 676, in generic
    return self.request(**r)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1092, in request
    self.check_exception(response)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 805, in check_exception
    raise exc_value
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 104, in view
    return self.dispatch(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 143, in dispatch
    return handler(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 154, in get
    self.object_list = self.get_queryset()
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 36, in get_queryset
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: IndexView is missing a QuerySet. Define IndexView.model, IndexView.queryset, or override IndexView.get_queryset().

======================================================================
ERROR: test_past_question (polls.tests.QuestionIndexViewTests)
# Questions with a pub_date in the past are displayed on the
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Django_Polls_App/mysite/polls/tests.py", line 62, in test_past_question
    response = self.client.get(reverse("polls:index"))
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1129, in get
    response = super().get(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 479, in get
    return self.generic(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 676, in generic
    return self.request(**r)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1092, in request
    self.check_exception(response)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 805, in check_exception
    raise exc_value
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 104, in view
    return self.dispatch(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 143, in dispatch
    return handler(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 154, in get
    self.object_list = self.get_queryset()
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 36, in get_queryset
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: IndexView is missing a QuerySet. Define IndexView.model, IndexView.queryset, or override IndexView.get_queryset().

======================================================================
ERROR: test_two_past_questions (polls.tests.QuestionIndexViewTests)
# The questions index page may display multiple questions.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Django_Polls_App/mysite/polls/tests.py", line 97, in test_two_past_questions
    response = self.client.get(reverse("polls:index"))
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1129, in get
    response = super().get(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 479, in get
    return self.generic(
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 676, in generic
    return self.request(**r)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 1092, in request
    self.check_exception(response)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/test/client.py", line 805, in check_exception
    raise exc_value
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 104, in view
    return self.dispatch(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/base.py", line 143, in dispatch
    return handler(request, *args, **kwargs)
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 154, in get
    self.object_list = self.get_queryset()
  File "/Django_Polls_App/venv/lib/python3.10/site-packages/django/views/generic/list.py", line 36, in get_queryset
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: IndexView is missing a QuerySet. Define IndexView.model, IndexView.queryset, or override IndexView.get_queryset().

----------------------------------------------------------------------
Ran 8 tests in 0.020s

FAILED (errors=6)
Destroying test database for alias 'default'...
```
