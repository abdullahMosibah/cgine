from django.urls import path
from django.views.generic import TemplateView

from cgine.main.views import category_view, lesson_view, prototype_page_view

app_name = "main"
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("demo/", view=prototype_page_view, name="prototype"),
    path("category/<category_id>", view=category_view, name="category"),
    path("lesson/<id>", view=lesson_view, name="lesson"),
    # path("category/<id>")
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
