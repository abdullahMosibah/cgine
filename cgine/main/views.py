from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import category, knowledge_block, lesson, membership
from .forms import lesson_form, knowledge_block_form
from django.http import JsonResponse


# Create your views here.
'''
TODO:
edit the forms system.
how to edit a lesson.
click on edit at the lesson page, and redirect to a dadicated edit page for that lesson.

how to edit a knowledge block
click on edit at the individual, knowledge block and you will be redicred to a dadicated edit page

how to add a knowledge block
click on add at the lesson page.
'''
@login_required
def dashboard_view(request):
    PUBLIC = "public"
    lesson_form_qs = lesson_form
    personal_lesson_qs = lesson.objects.filter(author=request.user)
    community_lessons_qs = lesson.objects.filter(status=PUBLIC)
    membership_qs = get_object_or_404(membership, user=request.user)
    context = {"lessons": personal_lesson_qs,
               "membership": membership_qs,
               "public_lessons": community_lessons_qs,
               "lesson_form": lesson_form_qs}
    return render(request, context=context, template_name="pages/dashboard.html")


def add_lesson_json(request):
    if request.method == "POST":
        new_form = lesson_form(request.POST)
        if new_form.is_valid():
            new_form.instance.author = request.user
            new_form.save()
    return JsonResponse({"status": "success"})


def edit_lesson(request, id):
    lesson_qs = get_object_or_404(lesson, id=id)
    knowledge_blocks_qs = knowledge_block.objects.filter(lesson=lesson_qs)
    knowledge_blocks_form_qs = knowledge_block_form
    context = {"lesson": lesson_qs,
               "knowledge_blocks": knowledge_blocks_qs,
               "knowledge_block_form": knowledge_blocks_form_qs,
               }

    return render(request, context=context, template_name="pages/edit_lesson.html")


def edit_lesson_json(request):
    if request.method == "POST":
        new_form = knowledge_block_form(request.POST)
        if new_form.is_valid():
            # add the rest data.
            new_form.save()
    return JsonResponse({"status": "success"})


def browse_view(request):
    PUBLIC = "public"
    community_lessons_qs = lesson.objects.filter(status=PUBLIC)
    context = {
        "public_lessons": community_lessons_qs,
    }
    return render(request, context=context, template_name="pages/browse.html")


def home_view(request):
    # TODO: pass the demo lesson from here to the landing page.
    context = {}
    return render(request, context=context, template_name="pages/home.html")


def lesson_view(request, category_id, id):
    lesson_qs = get_object_or_404(lesson, id=id)
    knowledge_blocks_qs = knowledge_block.objects.filter(lesson=lesson_qs)
    context = {
        "lesson": lesson_qs,
        "knowledge_blocks": knowledge_blocks_qs,
    }
    return render(
        request=request, context=context, template_name="pages/lesson_page.html"
    )


def category_view(request, category_id):
    category_qs = get_object_or_404(category, id=category_id)
    lesson_qs = lesson.objects.filter(category=category_qs)
    context = {
        "category": category_qs,
        "lessons": lesson_qs,
    }
    return render(
        request=request, context=context, template_name="pages/category_page.html"
    )
