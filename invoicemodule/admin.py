from django.contrib import admin
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1  # Number of empty forms to display in the inline formset

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    list_display = ('invoice_id', 'date', 'user', 'status')
    search_fields = ('invoice_id', 'user__username')

# Registering the models with the admin site
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem)  # Register InvoiceItem if you want to manage it separately
