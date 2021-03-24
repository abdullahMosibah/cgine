from django.urls import path

from cgine.main.views import prototype_page_view

app_name = "main"
urlpatterns = [
    path("demo/", view=prototype_page_view, name="prototype"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
