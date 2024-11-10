from django.contrib import admin

from .models import Tag

admin.site.register(Tag,)

# class TagAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'description',
#         'is_published',
#         'slug',
#     )
#     list_editable = (
#         'is_published',
#         'slug',
#     )
#     # search_fields = ('title', 'slug',)
#     # list_filter = ('title', 'slug',)
#     list_display_links = ('title',)

# admin.site.register(Tag,)
