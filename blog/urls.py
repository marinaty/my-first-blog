from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'sitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.listar_publicaciones),
    #url(r'crear/', views.crear_publicaciones), #na mas pa mientras
]
