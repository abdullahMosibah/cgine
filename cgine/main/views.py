from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import category, knowledge_block, lesson, membership
from .forms import lesson_form, knowledge_block_form
from django.http import JsonResponse
from django.views.generic.edit import FormView, UpdateView, CreateView

# Create your views here.

'''
TODO:
1- edit knowledge blocks(done)
2- add knowledge blocks(done)

3- regex on javascript
4- new knowledge block concept

5-start adding calc2
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


class edit_knowledge_block(UpdateView):
    model = knowledge_block
    fields = ["title", "content", "video", "audio", "resource", "glossary"]
    template_name = "pages/edit_knowledge_block.html"
    #success_url = "/dashboard"


class add_knowledge_block(CreateView):
    model = knowledge_block
    fields = ["lesson","title", "content", "video", "audio", "resource", "glossary"]
    template_name = "pages/add_knowledge_block.html"

'''
def edit_knowledge_block(request, id):
    knowledge_block_qs = get_object_or_404(knowledge_block, id=id)
    knowledge_block_form_qs = knowledge_block_form

    context = {
        "knowledge_block": knowledge_block_qs,
        "knowledge_block_form": knowledge_block_form_qs
    }

    return render(request, context=context, template_name="pages/edit_knowledge_block.html")

def edit_knowledge_block_json(request):
    if request.method == "POST":
        new_form = knowledge_block_form(request.POST)
        if new_form.is_valid():
            # add the rest data.
            new_form.save()
    return JsonResponse({"status": "success"})
'''


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
    PUBLIC = "public"
    community_lessons_qs = lesson.objects.filter(category=category_qs,status=PUBLIC)
    context = {
        "category": category_qs,
        "lessons": community_lessons_qs,
    }
    return render(
        request=request, context=context, template_name="pages/category_page.html"
    )
