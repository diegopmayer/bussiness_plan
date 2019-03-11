from django.contrib import admin
from .models import (
    ParceiroModel, 
    AtividadeModel,
    RecursoModel,
    PropostaModel,
    RelacionamentoModel,
    CanalModel,
    SegmentoModel,
    CustoModel,
    ReceitaModel
)


admin.site.register(ParceiroModel)
admin.site.register(AtividadeModel)
admin.site.register(RecursoModel)
admin.site.register(PropostaModel)
admin.site.register(RelacionamentoModel)
admin.site.register(CanalModel)
admin.site.register(SegmentoModel)
admin.site.register(CustoModel)
admin.site.register(ReceitaModel)
