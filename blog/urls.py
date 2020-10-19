from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
                path('', listar_publicaciones, name='listar_publicaciones'),
                path('<uuid:pub>/', ver_publicacion, name='ver_publicacion'),
                path('', ver_publicaciones_categoria, name='ver_publicaciones_categoria'),
]


