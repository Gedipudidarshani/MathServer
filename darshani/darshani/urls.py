from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('TSAofsquareprism/',views.squareprism,name="TSAofsquareprism"),
    path('',views.squareprism,name="TSAofsquareprismroot")
]