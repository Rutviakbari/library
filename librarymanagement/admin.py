
from django.contrib import admin


from.models import Author, User,Book,publisher,reader
admin.site.register(Book)

admin.site.register(Author)
admin.site.register(User)
admin.site.register(publisher)
admin.site.register(reader)



