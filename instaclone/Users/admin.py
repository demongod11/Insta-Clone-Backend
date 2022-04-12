from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Users.models import User


class AccountAdmin(UserAdmin):
    list_display = ('pk', 'email', 'username', 'fullname', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('pk', 'email', 'fullname', 'username',)
    readonly_fields = ('pk', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AccountAdmin)
