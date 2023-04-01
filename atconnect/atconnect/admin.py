from django.contrib import admin
from .models import Profile, System_Post
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ProfileInLine(admin.StackedInline):
    model = Profile

class CustomUserAdmin(UserAdmin):
    inclines = [ProfileInLine]

class UserAdmin(admin.ModelAdmin):
    #list_display = ('title', 'created_at', 'author')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(System_Post, UserAdmin)