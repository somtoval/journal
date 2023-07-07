from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("journal/<str:pk>/", views.journal, name="journal"),
    path("volume/<str:pk>/", views.volume, name="volume"),
    path("paper/<str:pk>/", views.paper_view, name="paper"),
    path("issue/<str:pk>/", views.issue_page, name="issue"),
    path("submit/", views.submit, name="submit"),
    path("all-journals", views.all_journals, name="all-journals"),
    path("topics", views.topics, name="topics"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("authors", views.authors, name="authors"),
    path("reviewers", views.reviewers, name="reviewers"),
    path("editors", views.editors, name="editors"),
    path("editorialProcess", views.editorialProcess, name="editorialProcess"),
    path("open-access", views.openAccessPolicy, name="open-access"),
    path("article-processing-charges", views.charges, name="ethics"),
    path("research-and-publication-ethics", views.ethics, name="charges"),
]