from django.urls import path
from index.views import Home

app_name = "index"


urlpatterns = [
    path('', Home, name="index")
]
