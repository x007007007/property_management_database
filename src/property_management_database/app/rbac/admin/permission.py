from django.contrib import admin
from ..models import PermissionModel


@admin.register(PermissionModel)
class PermissionModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return super(PermissionModelAdmin, self).get_queryset(request).select_related(
            'dj_perm',
            'type',
            'perm_config',
            'dj_perm__content_type'
        )

    def get_field_queryset(self, db, db_field, request):
        qs = super(PermissionModelAdmin, self).get_field_queryset(db, db_field, request)
        if db_field.name == 'dj_perm':
            if not qs:
                qs = db_field.related_model.objects.all()
            qs = qs.select_related('content_type')
        return qs

    search_fields = (
        'type__name',
        'dj_perm__name',
        'perm_config__name',
    )

    list_display = (
        'pk',
        'type',
        'dj_perm',
        'perm_config'
    )

    list_filter = (
        'type',
    )

    autocomplete_fields = (
        'perm_config',
    )