from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import category, knowledge_block, lesson, membership


# Create your views here.

@login_required
def dashboard_view(request):
    PUBLIC = "public"
    personal_lesson_qs = lesson.objects.filter(author=request.user)
    community_lessons_qs = lesson.objects.filter(status=PUBLIC)
    membership_qs = get_object_or_404(membership, user=request.user)
    context = {"lessons": personal_lesson_qs,
               "membership": membership_qs,
               "public_lessons":community_lessons_qs}
    return render(request, context=context, template_name="pages/dashboard.html")

def browse_view(request):
    PUBLIC = "public"
    community_lessons_qs = lesson.objects.filter(status=PUBLIC)
    context = {
      "public_lessons"  : community_lessons_qs,
    }
    return render(request,  context=context, template_name="pages/browse.html")
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
