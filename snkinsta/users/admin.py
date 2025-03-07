"""User admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    filter_horizontal = ('followers',)
    list_display_links = ('pk', 'user',)
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),('followers'),

            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'
    filter_horizontal = ('followers',)

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)