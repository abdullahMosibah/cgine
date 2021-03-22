from django.shortcuts import render


# Create your views here.
def prototype_page_view(request):

    return render(request=request, template_name="pages/prototype_page.html")
