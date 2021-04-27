from django.shortcuts import get_object_or_404, render

from .models import knowledge_block, lesson


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
