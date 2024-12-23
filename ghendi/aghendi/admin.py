from django.contrib import admin
from .models import Agenda, AgendaSection, AgendaElement, ElementComment

# Register the Agenda model in the Django admin interface
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    # Display the following fields in the agenda list view
    list_display = ('name', 'creator', 'id')
    
    # Provide a horizontal filter for the editors and members fields (many-to-many relationships)
    filter_horizontal = ('editors', 'members')


# Register the AgendaSection model in the Django admin interface
@admin.register(AgendaSection)
class AgendaSectionAdmin(admin.ModelAdmin):
    # Display the following fields in the section list view
    list_display = ('name', 'agenda', 'id')


# Register the AgendaElement model in the Django admin interface
@admin.register(AgendaElement)
class AgendaElementAdmin(admin.ModelAdmin):
    # Display the following fields in the element list view
    list_display = ('subject', 'section', 'emission', 'deadline')


# Register the ElementComment model in the Django admin interface
@admin.register(ElementComment)
class ElementCommentAdmin(admin.ModelAdmin):
    # Display the following fields in the comment list view
    list_display = ('user', 'element', 'created_at')