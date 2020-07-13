from django.contrib import admin
from .models import Poll, Question


class PollAdmin(admin.ModelAdmin):
    model = Poll
    list_display = ['title', 'description', 'start_pub', 'end_pub']
    list_editable = ['title', 'description', 'end_pub']
    list_display_links = None
    list_select_related = False


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['poll', 'title', 'kind']


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)