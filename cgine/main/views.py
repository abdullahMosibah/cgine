from django.shortcuts import get_object_or_404, render

from .models import category, knowledge_block, lesson


# Create your views here.
def prototype_page_view(request):
    return render(request=request, template_name="pages/prototype_page.html")


def lesson_view(request, id):
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
