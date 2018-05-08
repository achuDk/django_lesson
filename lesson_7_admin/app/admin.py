from django.contrib import admin
from app import models
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','issue_date','publish')
    list_editable = ('name','price')
    filter_horizontal = ('publish__name',)
    list_per_page = 2
    search_fields = ('id','name','issue_date')
    list_filter = ('issue_date','publish')

admin.site.register(models.Author)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Publish)
admin.site.register(models.Book_Author)