# Django Facebook shares count

Django app to store Facebook number of shares. It's using generic relations to store number of likes/shares of your 
webpages' various models with abosolute urls. 
 
## Instalation

```
pip install git+git://github.com/vlinhart/django_shares_count.git#egg=shares_count-dev
```
 
## Usage
 
In `settings.py`
 
```python
INSTALLED_APPS = (
...
    'shares_count',
)

SHARER_MODELS = ['core.Post',] 
```

The models specified in `SHARER_MODELS` must have method `get_full_url` which returns full url for which 
you want to find out how many shares it has. There must also be a datetime field `created` with the model's  
creation timestamp.
 
There is also a template filter which will output number of objects' shares.
 
 
```html
{% load shares_count_tags %}
{{ object|share_count }}({{ shares }}x)
```


To get the number of shares periodically, use the provided management command in a CRON. For example like this:
  
```
@monthly python manage.py update_shares.sh geront
@weekly python manage.py mature
@daily python manage.py teen
@hourly python manage.py new
```

The age of models is split in 4 categories which are updated with different frequencies.
