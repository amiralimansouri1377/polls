from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.detail_poll, name="detail-poll"),
    path("vote", views.VoteView.as_view(), name="vote")
]
