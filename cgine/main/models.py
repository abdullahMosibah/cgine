import uuid

from django.db import models


class lesson(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True, unique=True
    )
    time_added = models.DateField(auto_now_add=True)
    help_text = "the main layer of the lesson"
    title = models.CharField(max_length=80, default="new lesson")
    # TODO: knowledge block count + add index content
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    @property
    def get_knowledge_block(self):
        return self.knowledge_blocks.object.all()


class knowledge_block(models.Model):
    lesson = models.ForeignKey(
        lesson, related_name="knowledge_blocks", null=True, on_delete=models.CASCADE
    )
    content = models.TextField()
    video = models.FileField(upload_to="videos/%y/%m/")
    audio = models.FileField(upload_to="audios/%y/%m", null=True)
    resource = models.TextField()

    # def __str__(self):
    @property
    def get_quiz(self):
        return self.quiz.objects.all()


class quiz(models.Model):
    knowledge_block = models.ForeignKey(
        lesson, related_name="quiz", null=True, on_delete=models.CASCADE
    )
