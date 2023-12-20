from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    empty_value_display = "--empty--"
    list_display = ("username","email","contact","location")
    search_fields = ("username","bio")
    list_per_page = 100
    search_help_text = "search by ..."
    date_hierarchy = "date_joined"



    fieldsets = (
        (None, {"fields": ("username", "password")}),
		(_("Personal Info"), {"fields": ("username","first_name", "last_name", "email", "contact","profile_pic","bio","location","friends")}),
		(
			_("Permissions"),
			{
				"fields": (
					"is_active",
					"is_staff",
					"is_superuser",
					"groups",
					"user_permissions",
				),
			},
		),
		(_("Important dates"), {"fields": ("last_login", "date_joined")}),
	)
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2")
            }),
        )
