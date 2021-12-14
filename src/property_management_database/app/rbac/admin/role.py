from django.contrib import admin
from ..models import RoleModel


@admin.register(RoleModel)
class RoleModelAdmin(admin.ModelAdmin):

    def get_field_queryset(self, db, db_field, request):
        qs = super(RoleModelAdmin, self).get_field_queryset(db, db_field, request)
        if db_field.name == 'permission_set':
            if not qs:
                qs = db_field.related_model.objects.all()
            qs = qs.select_related(
                'dj_perm',
                'dj_perm__content_type',
                'perm_config',
                'type',
            )
        return qs

    list_display = (    )

    autocomplete_fields = (
        # 'permission_set',
        # 'auth_group',
    )