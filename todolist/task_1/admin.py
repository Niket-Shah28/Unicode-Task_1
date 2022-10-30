from django.contrib import admin
from .models import register1,todo
# Register your models here.
@admin.register(register1)
class userAdmin(admin.ModelAdmin):
    list_display=('username','first_name','last_name','email','profile_picture')

@admin.register(todo)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','Title','Note','Count','Save_Date','name','Last_Date','Status')
    search_fields=('Title',)