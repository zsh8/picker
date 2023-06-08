from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('storage/', include('storage.urls'))

]
urlpatterns += staticfiles_urlpatterns()
