from django.urls.conf import path
from .views import BlogList


urlpatterns = [path('',BlogList.as_view()), ]