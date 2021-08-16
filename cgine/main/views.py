from django.shortcuts import get_object_or_404, render
from .models import category, knowledge_block, lesson, membership, quiz
from .forms import lesson_form, knowledge_block_form
from django.http import JsonResponse
from django.views.generic.edit import  UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

'''

'''



def home_view(request):
    # TODO: pass the demo lesson from here to the landing page.
    context = {}
    return render(request, context=context, template_name="pages/home.html")

@login_required
def dashboard_view(request):
    PUBLIC = "public"
    lesson_form_qs = lesson_form
    personal_lesson_qs = lesson.objects.filter(author=request.user)
    community_lessons_qs = lesson.objects.filter(status=PUBLIC)
    #membership_qs = get_object_or_404(membership, user=request.user)
    membership_qs = membership.objects.filter(user=request.user)
    '''
    this is a quick fix for signups,
    later make it get or 404.
    and when creating account, automate associating it with a memebership, so we dont get 404s.
    also change the html,that retrives membership data.
    '''
    context = {"lessons": personal_lesson_qs,
               "membership": membership_qs,
               "public_lessons": community_lessons_qs,
               "lesson_form": lesson_form_qs}
    return render(request, context=context, template_name="pages/dashboard.html")

def browse_view(request):
    PUBLIC = "public"
    community_lessons_qs = lesson.objects.filter(status=PUBLIC)
    context = {
        "public_lessons": community_lessons_qs,
    }
    return render(request, context=context, template_name="pages/browse.html")


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

def add_lesson_json(request):
    if request.method == "POST":
        new_form = lesson_form(request.POST)
        if new_form.is_valid():
            new_form.instance.author = request.user
            new_form.save()
    return JsonResponse({"status": "success"})

@method_decorator(login_required, name="dispatch")
class edit_lesson(UpdateView):
    model = lesson
    fields = ["title", "description", "category", "status"]
    template_name = "pages/edit_lesson.html"

@method_decorator(login_required, name="dispatch")
class delete_lesson(DeleteView):
    model = lesson
    template_name = "pages/delete_lesson.html"
    success_url = reverse_lazy("main:dashboard")




@method_decorator(login_required, name="dispatch")
class add_knowledge_block(CreateView):
    model = knowledge_block
    fields = ["lesson","title", "content", "video", "audio", "resource", "glossary"]
    template_name = "pages/add_knowledge_block.html"

@method_decorator(login_required, name="dispatch")
class edit_knowledge_block(UpdateView):
    model = knowledge_block
    fields = ["title", "content", "video", "audio", "resource", "glossary"]
    template_name = "pages/edit_knowledge_block.html"
    #success_url = "/dashboard"

@method_decorator(login_required, name="dispatch")
class delete_knowledge_block(DeleteView):
    model = knowledge_block
    template_name = "pages/delete_knowledge_block.html"
    success_url = reverse_lazy('main:dashboard')


@login_required
class add_quiz(CreateView):
    model = quiz
    fields = ["knowledge_block"]
    template_name = "pages/add_quiz.html"
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





