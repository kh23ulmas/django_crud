from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.


# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Language)
# admin.site.register(Author)
admin.site.register(Genre)

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

# Define admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')    
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)