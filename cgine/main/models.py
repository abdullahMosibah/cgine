import uuid

# from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class category(models.Model):
    name = models.CharField(max_length=100, null=True)
    icon = models.FileField(upload_to="category_icons/")

    @property
    def get_lessons(self):
        return self.lessons.all().order_by("time_added")

    def get_absolute_url(self):
        return f"/category/{self.id}"

    # temporary fix  for category url


class lesson(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True, unique=True
    )
    category = models.ForeignKey(
        category, related_name="lessons", null=True, on_delete=models.CASCADE
    )
    time_added = models.DateField(auto_now_add=True)
    help_text = "the main layer of the lesson"
    title = models.CharField(max_length=80, default="new lesson")
    icon = models.FileField(upload_to="images/", null=True)
    # TODO: knowledge block count + add index content
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    @property
    def get_knowledge_blocks(self):
        return self.knowledge_blocks.all().order_by("time_added")

    def get_absolute_url(self):
        return f"/category/{self.category_id}/lesson/{self.id}"



class knowledge_block(models.Model):
    lesson = models.ForeignKey(
        lesson, related_name="knowledge_blocks", null=True, on_delete=models.CASCADE
    )
    time_added = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField()
    video = models.FileField(upload_to="videos/")
    audio = models.FileField(upload_to="audios/", null=True)
    resource = models.TextField()

    # def __str__(self):
    @property
    def get_quiz(self):
        return self.quiz



class quiz(models.Model):
    knowledge_block = models.ForeignKey(
        lesson, related_name="quiz", null=True, on_delete=models.CASCADE
    )

