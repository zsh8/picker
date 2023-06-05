from django.urls import path, include

urlpatterns = [
    path('storage/', include('storage.urls'))
]
