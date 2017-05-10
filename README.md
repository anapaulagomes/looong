# Looong

Keeping eyes on long parameters list 🔍

[![Build Status](https://travis-ci.org/anapaulagomes/looong.svg?branch=master)](https://travis-ci.org/anapaulagomes/looong) [![Code Climate](https://codeclimate.com/github/anapaulagomes/looong/badges/gpa.svg)](https://codeclimate.com/github/anapaulagomes/looong) [![Code Health](https://landscape.io/github/anapaulagomes/looong/master/landscape.svg?style=flat)](https://landscape.io/github/anapaulagomes/looong/master)

Long parameter list is a code smell - a clue that there is a problem on your software design. To help you on this this module has been written to identify methods with long parameter list and to suggest parameters groups that could became potential object because they appear together.

### Running

`python looong/main.py -d tests/repos/django-master`

- Output:

```
Analyzed files: 553
Analyzed methods: 2224

render [tests/repos/django-master/django/shortcuts.py] ['request', 'template_name', 'context', 'content_type', 'status', 'using'] 6
create [tests/repos/django-master/django/contrib/admin/filters.py] ['field', 'request', 'params', 'model', 'model_admin', 'field_path'] 6
kml [tests/repos/django-master/django/contrib/gis/sitemaps/views.py] ['request', 'label', 'model', 'field_name', 'compress', 'using'] 6
run [tests/repos/django-master/django/core/servers/basehttp.py] ['addr', 'port', 'wsgi_handler', 'ipv6', 'threading', 'server_cls'] 6
data [tests/repos/django-master/django/contrib/gis/gdal/raster/band.py] ['data', 'offset', 'size', 'shape', 'as_memoryview'] 5
kmz [tests/repos/django-master/django/contrib/gis/sitemaps/views.py] ['request', 'label', 'model', 'field_name', 'using'] 5
dumps [tests/repos/django-master/django/core/signing.py] ['obj', 'key', 'salt', 'serializer', 'compress'] 5
loads [tests/repos/django-master/django/core/signing.py] ['s', 'key', 'salt', 'serializer', 'max_age'] 5
migrate [tests/repos/django-master/django/db/migrations/executor.py] ['targets', 'plan', 'state', 'fake', 'fake_initial'] 5
connect [tests/repos/django-master/django/db/models/signals.py] ['receiver', 'sender', 'weak', 'dispatch_uid', 'apps'] 5
```

### Goal

```
LoooooooooooooooooooooooooooooooooooG

method_name [file_name] [params] - number of parameters

Correlated parameters and possible objects:

(foo, bar)
(foo, bar, barbar)

```

### Development

Running the tests:

`pytest tests/`

`pytest --cov=looong tests/`
