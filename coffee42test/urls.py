# -- coding: utf-8 --
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static

from apps.chamber.views import (
							SirListView,
							# SirUpdateView,
							RequestContetnView,
						)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', SirListView.as_view(), name='home'),
	url(r'^request/$', RequestContetnView.as_view(), name='request'),
	# url(r'^edit/(?P<pk>\d+)/$', SirUpdateView.as_view(), name='edit'),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
		)
