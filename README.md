# Looong

Keeping eyes on long parameters list 🔍

[![Build Status](https://travis-ci.org/anapaulagomes/looong.svg?branch=master)](https://travis-ci.org/anapaulagomes/looong) [![Code Climate](https://codeclimate.com/github/anapaulagomes/looong/badges/gpa.svg)](https://codeclimate.com/github/anapaulagomes/looong) [![Code Health](https://landscape.io/github/anapaulagomes/looong/master/landscape.svg?style=flat)](https://landscape.io/github/anapaulagomes/looong/master)


Long parameter list is a code smell - a clue that there is a problem on your software design. To help you on this this module has been written to identify methods with long parameter list and to suggest parameters groups that could became potential object because they appear together.

### Goal

`looong source/`

- Output:

```
Record:

method_name.file_name - number of parameters

Correlated parameters:

(foo, bar)
(foo, bar, barbar)

```

### Development

`pytest tests/`

`pytest --cov=looong tests/`
