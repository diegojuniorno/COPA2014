from django.conf.urls import patterns, include, url

urlpatterns = patterns('copa.views',
    url(r'^salvar/$', 'pessoaSalvar'),
)