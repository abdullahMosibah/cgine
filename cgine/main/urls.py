from django.urls import path
from django.views.generic import TemplateView

from cgine.main.views import category_view, home_view, lesson_view, dashboard_view, browse_view, add_lesson_json,edit_knowledge_block, add_knowledge_block

app_name = "main"
urlpatterns = [
    path("", view=home_view, name="home"),
    path("category/<category_id>", view=category_view, name="category"),
    path("category/<category_id>/lesson/<id>", view=lesson_view, name="lesson"),
    path("dashboard", view=dashboard_view, name="dashboard"),
    path("browse", view=browse_view, name="browse"),
    path("add_lesson/", view=add_lesson_json, name="add_lesson"),
    path("edit/knowledge_block/<pk>/", view=edit_knowledge_block.as_view(), name= "edit_knowledge_block"),
    path("add/knowledge_block/", view=add_knowledge_block.as_view(), name="add_knowledge_block"),

    # path("category/<id>")
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
'''
as for lessons and knowledge blocks.
we have two views
one for loading the the page (lesson)
one for json response ( lesson_json)
'''
