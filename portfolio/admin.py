from django.contrib import admin
from portfolio.models import Contact, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'goal',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address')
    readonly_fields = ('name', 'email_address', 'message')
