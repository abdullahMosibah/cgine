from django.urls import path
from django.views.generic import TemplateView

from cgine.main.views import category_view, home_view, lesson_view, dashboard_view, browse_view, add_lesson_json, edit_lesson,edit_lesson_json

app_name = "main"
urlpatterns = [
    path("", view=home_view, name="home"),
    path("category/<category_id>", view=category_view, name="category"),
    path("category/<category_id>/lesson/<id>", view=lesson_view, name="lesson"),
    path("edit/lesson/<id>", view=edit_lesson, name="edit_lesson"),
    path("edit_lesson/", view=edit_lesson_json, name="edit_lesson"),
    path("dashboard", view=dashboard_view, name="dashboard"),
    path("browse", view=browse_view, name="browse"),
    path("add_lesson/", view=add_lesson_json, name="add_lesson")
    # path("category/<id>")
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
