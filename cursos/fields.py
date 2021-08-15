from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrdenarCampos(models.PositiveIntegerField):
    def __init__(self, for_fiels=None, *args, **Kwargs):
        self.for_fields = for_fiels
        super().__init__(*args,**Kwargs)


    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)
                ultimo_item = qs.latest(self.attname)
                value = ultimo_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)