from django.urls import path

from cgine.main.views import lesson_view, prototype_page_view

app_name = "main"
urlpatterns = [
    path("demo/", view=prototype_page_view, name="prototype"),
    path("lesson/<id>", view=lesson_view, name="lesson")
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
