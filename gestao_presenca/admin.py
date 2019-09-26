from django.contrib import admin

from .models import Atividade
from .models import Inscricao

admin.site.register(Atividade)
admin.site.register(Inscricao)
