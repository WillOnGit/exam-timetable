from django.contrib import admin

from .models import Exam, Room, ExamVenue, InvigilatorResponse, ExamsAdmin, Invigilator

admin.site.register(Exam)
admin.site.register(Room)
admin.site.register(ExamVenue)
admin.site.register(InvigilatorResponse)
admin.site.register(ExamsAdmin)
admin.site.register(Invigilator)
