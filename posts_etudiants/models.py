from django.db import models
from django.contrib.auth.models import User

class ProfilEtudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    programme = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Post(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()    # Summernote gérera ce champ
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return f"/post/{self.pk}/"