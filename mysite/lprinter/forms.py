from django import forms
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from .models import Task
from django.contrib.auth.forms import UserCreationForm

















class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")





class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

        self.fields["status"].widget.attrs.update({"class": "form-select"})

        if request and request.user.is_superuser:
            self.fields["user"] = forms.ModelChoiceField(
                queryset=User.objects.order_by("username"),
                required=False,
                label="Vartotojas",
                widget=forms.Select(attrs={"class": "form-select"}),
            )
            if self.instance and self.instance.pk:
                self.fields["user"].initial = self.instance.user
        else:
            self.fields.pop("user", None)

    class Meta:
        model = Task
        fields = ["title", "content", "status", "user"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": TinyMCE()
        }



class TaskAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())


    class Meta:
        model = Task
        fields = "__all__"

