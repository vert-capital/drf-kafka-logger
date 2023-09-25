import json

from .models import Log
from django.contrib import admin
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer


@admin.register(Log)
class KafkaLogAdmin(admin.ModelAdmin):
    list_display = ["date", "content_type", "status"]
    list_display_links = ["date"]
    search_fields = ["date", "content_type"]
    list_filter = ["status",]
    ordering = ["date", "status"]
    raw_id_fields = ["content_type"]

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields] + ["data_prettified"]

    def has_delete_permission(self, request, obj=None):
        return False

    def data_prettified(self, instance):
        """Function to display pretty version of our data"""
        # Convert the data to sorted, indented JSON
        response = json.dumps(instance.data, sort_keys=True, indent=2,
                              default=str)

        # Truncate the data. Alter as needed
        # response = response[:5000]

        # Get the Pygments formatter
        formatter = HtmlFormatter()

        # Highlight the data
        response = highlight(response, JsonLexer(), formatter)

        # Get the stylesheet
        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        # Safe the output
        return mark_safe(style + response)

    data_prettified.short_description = "Dados Completos (Formatado)"
