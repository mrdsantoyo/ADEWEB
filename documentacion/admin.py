from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Normas

# Register your models here.


@admin.register(Normas)
class NormasAdmin(ImportExportModelAdmin):
    pass


