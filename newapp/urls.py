# Import the utility functions from the django urls library
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
      # Map the root URL / to be handled by
      # 'registration.views.registration_form' view
      url(r'^$', 'registration.views.registration_form'),

      # Allow the URLs beginning with /captcha/ to be handled by
      # the urls.py of captcha module from 'django-simple-captcha'
      url(r'^captcha/', include('captcha.urls')),
)




# from django.conf.urls import patterns, include, url
# from django.contrib import admin
#
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'newapp.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# )
