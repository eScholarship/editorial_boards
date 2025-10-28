from django.contrib import admin

from .models import Journal, Person, Institution, Issue, EditorialBoardMember

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'journal_url')
    search_fields = ('code', 'name')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'orcid')
    search_fields = ('first_name', 'last_name', 'email', 'orcid')

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'ror_id', 'city', 'country', 'is_uc')
    search_fields = ('name', 'ror_id', 'city', 'country')

class EditorialBoardMemberInline(admin.TabularInline):
    model = EditorialBoardMember
    extra = 1
    autocomplete_fields = ['person', 'affiliation'] 

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('journal', 'volume', 'issue_number', 'start_date', 'end_date', 'source_url')
    search_fields = ('journal__name', 'volume', 'issue_number')
    list_filter = ('journal',)
    inlines = [EditorialBoardMemberInline]
    autocomplete_fields = ['journal']

@admin.register(EditorialBoardMember)
class EditorialBoardMemberAdmin(admin.ModelAdmin):
    list_display = ('issue', 'person', 'affiliation', 'role')
    search_fields = ('person__first_name', 'person__last_name', 'role')
    list_filter = ('issue__journal', 'role')
    autocomplete_fields = ['person', 'affiliation'] 
