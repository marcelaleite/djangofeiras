from django.contrib import admin

from .models import Feira
from .models import Organizadores
from .models import Patrocinadores
from .models import Observacoes
from .models import Instituicao
from .models import Categoria

admin.site.register(Feira)
admin.site.register(Organizadores)
admin.site.register(Patrocinadores)
admin.site.register(Observacoes)
admin.site.register(Instituicao)
admin.site.register(Categoria)
