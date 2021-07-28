from django import forms
from .models import lesson, knowledge_block
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class lesson_form(forms.ModelForm):
    class Meta:
        model = lesson
        fields = ["title", "description", "category", "status"]


class knowledge_block_form(forms.ModelForm):
    class Meta:
        model = knowledge_block
        fields = ["title", "content", "video", "audio", "resource", "glossary"]
