from django.urls import path
from django.views.generic import TemplateView

from cgine.main.views import category_view, home_view, lesson_view

app_name = "main"
urlpatterns = [
    path("", view=home_view, name="home"),
    path("category/<category_id>", view=category_view, name="category"),
    path("category/<category_id>/lesson/<id>", view=lesson_view, name="lesson"),
    # path("category/<id>")
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
