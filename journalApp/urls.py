from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("journal/<str:pk>/", views.journal, name="journal"),
    path("volume/<str:pk>/", views.volume, name="volume"),
    path("paper/<str:pk>/", views.paper_view, name="paper")
]
