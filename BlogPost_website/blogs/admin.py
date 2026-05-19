from django.contrib import admin

from .models import *

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)

admin.site.site_header = "BLOGSPOST | ADMIN PANEL"
admin.site.site_title = "BLOGSPOST | BLOGGING WEBSITE"
admin.site.index_title = "Blogspost Site Administration"