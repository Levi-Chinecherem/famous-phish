from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import PhishingAttempt
from .views import custom_admin_dashboard

class CustomAdminSite(AdminSite):
    site_header = "Famous Phish Admin"
    site_title = "Famous Phish Admin"
    index_title = "Dashboard"

custom_admin_site = CustomAdminSite(name='customadmin')


class PhishingAttemptAdmin(admin.ModelAdmin):
    list_display = ('attacker_ip', 'target_url', 'success', 'timestamp')
    list_filter = ('success', 'timestamp')
    search_fields = ('attacker_ip', 'target_url')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

    # Customize the list view
    list_per_page = 10  # Number of items to display per page

    # Customize the detail view
    fieldsets = (
        ('Phishing Attempt Details', {
            'fields': ('attacker_ip', 'target_url', 'success', 'timestamp'),
        }),
    )

    # Add a read-only field
    readonly_fields = ('timestamp',)

custom_admin_site.register(PhishingAttempt, PhishingAttemptAdmin)

# Register the custom admin dashboard view
custom_admin_site.admin_view(custom_admin_dashboard, 'dashboard/')
