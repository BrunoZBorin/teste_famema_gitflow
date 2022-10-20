
from django.contrib import admin
from django.urls import path
from contas.views import home, listagem, update, nova_transacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('nova/', nova_transacao),
    path('', listagem),
    path('update/<int:pk>/', update, name='url_update')
]
