from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('payment.urls')),
    # url(r'^payment/', include('payment.urls')),
    url(r'^admin/', admin.site.urls),
]
