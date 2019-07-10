from django.contrib import admin

from .models import Exam, Room, ExamVenue

admin.site.register(Exam)
admin.site.register(Room)
admin.site.register(ExamVenue)
