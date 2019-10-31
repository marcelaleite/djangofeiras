from django.contrib import admin

from .models import Atividade
from .models import Inscricao
from .models import Cronograma

admin.site.register(Atividade)
admin.site.register(Inscricao)
admin.site.register(Cronograma)
