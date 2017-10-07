# Looong

Keeping eyes on long parameters list 🔍

[![Build Status](https://travis-ci.org/anapaulagomes/looong.svg?branch=master)](https://travis-ci.org/anapaulagomes/looong) [![Code Climate](https://codeclimate.com/github/anapaulagomes/looong/badges/gpa.svg)](https://codeclimate.com/github/anapaulagomes/looong) [![Code Health](https://landscape.io/github/anapaulagomes/looong/master/landscape.svg?style=flat)](https://landscape.io/github/anapaulagomes/looong/master)

Long parameter list is a code smell - a clue that there is a problem on your software design. To help you on this this module has been written to identify methods with long parameter list and to suggest parameters groups that could became potential object because they appear together.

## Usage

### Installing
```bash
$ make install
```

We recommend the use of virtual environment.

### Running
```bash
$ python looong/main.py -d <directory>
```

```bash
Analyzed files: 553
Analyzed methods: 2224

render [django/shortcuts.py] ['request', 'template_name', 'context', 'content_type', 'status', 'using'] 6
create [django/contrib/admin/filters.py] ['field', 'request', 'params', 'model', 'model_admin', 'field_path'] 6
kml [django/contrib/gis/sitemaps/views.py] ['request', 'label', 'model', 'field_name', 'compress', 'using'] 6
run [django/core/servers/basehttp.py] ['addr', 'port', 'wsgi_handler', 'ipv6', 'threading', 'server_cls'] 6
data [django/contrib/gis/gdal/raster/band.py] ['data', 'offset', 'size', 'shape', 'as_memoryview'] 5
kmz [django/contrib/gis/sitemaps/views.py] ['request', 'label', 'model', 'field_name', 'using'] 5
dumps [django/core/signing.py] ['obj', 'key', 'salt', 'serializer', 'compress'] 5
loads [django/core/signing.py] ['s', 'key', 'salt', 'serializer', 'max_age'] 5
migrate [django/db/migrations/executor.py] ['targets', 'plan', 'state', 'fake', 'fake_initial'] 5
connect [django/db/models/signals.py] ['receiver', 'sender', 'weak', 'dispatch_uid', 'apps'] 5
```

### Goal

Methods with long parameter list pointing to a problem with OO principles. One of the approach to solve is creating objects with the parameters that appear more together. Our goal is cluster this parameters and suggest as objects.

```
LoooooooooooooooooooooooooooooooooooG

Analyzed files: 553
Analyzed methods: 2224

render [django/shortcuts.py] ['request', 'template_name', 'context', 'content_type', 'status', 'using'] 6
create [django/contrib/admin/filters.py] ['field', 'request', 'params', 'model', 'model_admin', 'field_path'] 6
kml [django/contrib/gis/sitemaps/views.py] ['request', 'label', 'model', 'field_name', 'compress', 'using'] 6
run [django/core/servers/basehttp.py] ['addr', 'port', 'wsgi_handler', 'ipv6', 'threading', 'server_cls'] 6

Correlated parameters and possible objects:

(foo, bar)
(foo, bar, barbar)

```

## Development

Please see [our contribution guide](CONTRIBUTING.md).
