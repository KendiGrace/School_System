from django.forms import ModelForm, DateInput
from django.forms.widgets import TextInput, Textarea
from event.models import Events


class EventForm(ModelForm):
    class Meta:
        model = Events
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': DateInput(attrs={
                'type': 'datetime-local',
                'style': 'max-width: 300px;',
                'class': "form-control",
            },
                format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={
                'type': 'datetime-local',
                'style': 'max-width: 300px;',
                'class': "form-control",
            },
                format='%Y-%m-%dT%H:%M'),
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Event Title'
            }),
            'venue': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Event Venue'
            }),
            'description': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Description'
            })
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
