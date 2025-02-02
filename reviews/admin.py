from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn13')

admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)