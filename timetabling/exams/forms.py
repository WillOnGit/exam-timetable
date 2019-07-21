from .models import ExamVenue
from django.forms import ModelForm

class RestrictedResponseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RestrictedResponseForm, self).__init__(*args,**kwargs)
        try:
            self.fields['assigned_venue'].queryset = ExamVenue.objects.filter(exam=self.instance.exam)
        except:
            self.fields['assigned_venue'].queryset = ExamVenue.objects.none()
