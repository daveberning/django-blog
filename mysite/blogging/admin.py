from django.contrib import admin
from blogging.models import Post, Category, PostAdmin, CategoryAdmin

# and a new admin registration
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)