from django.contrib import admin

from .models import Exam, Room, ExamVenue, InvigilatorResponse
from .forms import RestrictedResponseForm

# register without modification
admin.site.register(Exam)
admin.site.register(Room)
admin.site.register(ExamVenue)

# custom admin classes
# restrict venue options
class ResponseAdmin(admin.ModelAdmin):
    form = RestrictedResponseForm
admin.site.register(InvigilatorResponse,ResponseAdmin)
