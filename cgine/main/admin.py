from django.contrib import admin

from .models import category, knowledge_block, lesson
# question, quiz, choice
admin.site.register(lesson)
admin.site.register(knowledge_block)
#admin.site.register(quiz)
admin.site.register(category)
#admin.site.register(choice)
#admin.site.register(question)
# Register your models here.
