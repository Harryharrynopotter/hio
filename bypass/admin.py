from django.contrib import admin
from .models import *
# Register your models here.

# list_display：控制模型的哪些字段可以显示在 admin 界面，其接收一个序列；
# list_display_links：控制 list_display 中哪些字段可以被链接到数据的修改页面；
# list_editable：设置哪些字段可以在列表中直接进行修改；
# list_filter：设置可以通过哪些字段对数据进行过滤筛选；
# search_fields：启用 admin 界面的搜索框，可以搜索指定的字段。


class BypassAdmin(admin.ModelAdmin):
    list_display = ['id', 'browser_name', 'bypass_key', 'created', 'bypass_status']
    list_editable = ['bypass_key']
    list_filter = ['bypass_status']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'item_price', 'item_update_time', 'is_show']
    list_filter = ['is_show']
    search_fields = ['item_name']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'task_status', 'is_on', 'task_update_time', 'is_delete']
    list_filter = ['task_status', 'is_on', 'is_delete']


admin.site.register(Bypass, BypassAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Task, TaskAdmin)








