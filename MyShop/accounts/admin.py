from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models import User
from django.utils.html import format_html

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    def image_tag(self, obj):
        try:
            return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.profile_picture.url))
        except:
            pass

    list_display = ('username', 'email', 'phone_number', 'gender', 'image_tag', 'is_admin')
    list_filter = ('is_admin', 'is_active')

    fieldsets = (
        ('User', {'fields': ('username', 'email', 'phone_number', 'full_name', 'date_of_birth', 'gender', 'profile_picture', 'password')}),
        (None, {'fields': ('is_active', 'is_admin', 'last_login')}),
    )


    add_fieldsets = (
        ('User Creation', {'fields': ('username', 'email', 'phone_number', 'full_name', 'date_of_birth', 'gender', 'profile_picture', 'password1', 'password2')}),
        (None, {'fields': ('is_admin', )}),
    )

    search_fields = ('email', 'full_name')

    ordering = ('email', )


    filter_horizontal = ()



admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
