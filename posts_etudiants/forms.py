from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfilEtudiant, Post
from django_summernote.widgets import SummernoteWidget

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nom = forms.CharField(max_length=100, required=True)
    prenom = forms.CharField(max_length=100, required=True)
    programme = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'nom', 'prenom', 'programme', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            ProfilEtudiant.objects.create(
                user=user,
                nom=self.cleaned_data['nom'],
                prenom=self.cleaned_data['prenom'],
                programme=self.cleaned_data['programme']
            )
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titre', 'contenu']
        widgets = {
            'contenu': SummernoteWidget(),  # Utilisation de Summernote pour le contenu
        }