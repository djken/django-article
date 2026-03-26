from django.contrib import admin
from .models import Post, ProfilEtudiant
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('contenu',)

admin.site.register(Post, PostAdmin)
admin.site.register(ProfilEtudiant)