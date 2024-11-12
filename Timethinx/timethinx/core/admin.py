from django.contrib import admin

from .models import Customer, Project, Task, TaskLog, User
from daterangefilter.filters import DateRangeFilter


# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username/
# Author: Federico Jaramillo Martínez
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'part_time')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', ('first_name', 'last_name'), 'part_time', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'part_time', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'part_time')
    list_filter = ('part_time',)
    ordering = ('email',)

class BaseAdmin(admin.ModelAdmin):
    class Meta:
        abstract = True


class CustomerAdmin(BaseAdmin):
    list_display = ("customer_name",)
    search_fields = ("customer_name",)


class ProjectAdmin(BaseAdmin):
    list_display = ("project_name", "customer")
    search_fields = ("project_name", "customer__customer_name")
    list_filter = ("customer",)
    raw_id_fields = ("customer",)


class TaskAdmin(BaseAdmin):
    list_display = ("task_name", "project", "get_user")
    search_fields = ("task_name", "project__project_name", "user__first_name", "user__last_name")
    list_filter = ("project",)
    raw_id_fields = ("project", "user")

    def get_user(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    get_user.short_description = "Çalışan"

    def get_queryset(self, request):
        qs = super(TaskAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class TaskLogAdmin(BaseAdmin):
    list_display = ("get_user", "task", "hours_worked", "created_at")
    search_fields = ("task__task_name", "task__user__first_name", "task__user__last_name", "task__project__project_name"
                     , "task__project__customer__customer_name")
    list_filter = (("created_at", DateRangeFilter), "task__project__customer__customer_name", "task__project")
    raw_id_fields = ("task",)
    ordering = ("-created_at",)

    def get_user(self, obj):
        return f'{obj.task.user.first_name} {obj.task.user.last_name}'
    get_user.short_description = "Çalışan"

    def get_queryset(self, request):
        qs = super(TaskLogAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(task__user=request.user)

admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskLog, TaskLogAdmin)
