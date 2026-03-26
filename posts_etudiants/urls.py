from django.urls import path
from .views import signup, liste_posts, post_create, post_detail, post_update, post_delete

urlpatterns = [
    path('', liste_posts, name='liste_posts'),
    path('post/creer/', post_create, name='creer_post'),
    path('post/<int:pk>/', post_detail, name='detail_post'),
    path('post/<int:pk>/modifier/', post_update, name='modifier_post'),
    path('post/<int:pk>/supprimer/', post_delete, name='supprimer_post'),
    path('signup/', signup, name='signup'),
]

