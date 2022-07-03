from django.contrib import admin
from quikapp.models import  UserProfile
#from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(UserProfile)


"""class CustomUserAdmin(UserAdmin):
model = CustomUser
list_display = ('email', 'is_staff', 'is_active',)
list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

#admin.site.register(CustomUser, CustomUserAdmin)"""