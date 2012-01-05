from django.conf.urls.defaults import *

urlpatterns = patterns('tokenapi.views',
    url(r'^token/new.json$', 'token_new', name='api_token_new'),
    url(r'^token/validate.json$', 'token', name='api_token'),
)
