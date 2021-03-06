import uuid

from django.db import models
import cgine.users.models as user
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import  RichTextUploadingField


class category(models.Model):
    app_label = "main"
    name = models.CharField(max_length=100, null=True)
    icon = models.FileField(upload_to="category_icons/")

    def __str__(self):
        return  str(self.id) + " " + self.name

    @property
    def get_lessons(self):
        return self.lessons.all().order_by("time_added")

    def get_absolute_url(self):
        return f"/category/{self.id}"
    # temporary fix  for category url

class lesson(models.Model):
    #TODO: add the enterprise options.
    PUBLIC = "public"
    PRIVATE = "private"

    STATUS= [
        (PUBLIC,  'community public'),
        (PRIVATE, 'private'),
    ]

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True, unique=True
    )
    author = models.ForeignKey(user.User, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=9,choices=STATUS, null=True,default=PUBLIC)
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

    def get_edit_url(self):
        return f"/edit/lesson/{self.id}"

    def get_delete_url(self):
        return f"/delete/lesson/{self.id}"


class knowledge_block(models.Model):
    title = models.CharField(max_length=100, default="new knowledge Block", null=True)
    lesson = models.ForeignKey(
        lesson, related_name="knowledge_blocks", null=True, on_delete=models.CASCADE
    )
    time_added = models.DateTimeField(auto_now_add=True, null=True)
    content = RichTextUploadingField(blank=True,null=True)
    video = models.FileField(upload_to="videos/")
    audio = models.FileField(blank=True,upload_to="audios/", null=True)
    resource = RichTextUploadingField(blank=True,null=True)
    glossary = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.title

    @property
    def get_titles(self):
        return self.title

    def get_quiz(self):
        return self.quiz.all()

    def get_edit_url(self):
        return f"/edit/knowledge_block/{self.id}"

    def get_delete_url(self):
        return f"/delete/knowledge_block/{self.id}"

    def get_absolute_url(self):
        return f"/category/{self.lesson.category_id}/lesson/{self.lesson.id}"


class quiz(models.Model):
    knowledge_block = models.ForeignKey(
        knowledge_block, related_name="quiz", null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.knowledge_block.title + " quiz"

    @property
    def get_questions(self):
        return self.questions.all()


class question(models.Model):
    content = RichTextUploadingField(blank=True,null=True, default="a question")
    quiz = models.ForeignKey(
        quiz, related_name="questions", null=True, on_delete=models.CASCADE
    )
    #its tricky to define a str for questoion, because content is an html. so it wont appear and admin as a normal string,
    #find a solution for this later, use a regex or something idk. gg
    def __str__(self):
        return str(self.content)

    def get_choices(self):
        return self.choices.all()


# how to check for which choice is correct.


class choice(models.Model):
    content = models.TextField(blank=True,null=True)
    is_correct = models.BooleanField()
    question = models.ForeignKey(
        question, null=True, related_name="choices", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.content


class plan(models.Model):
    name = models.CharField(max_length=254)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class membership(models.Model):
    user = models.ForeignKey(user.User,null=True, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.ForeignKey(plan, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return   str( self.user)

# 1 lesson => m knowledgeBlocks --> 1 quiz --> m questions
#m = multiple


