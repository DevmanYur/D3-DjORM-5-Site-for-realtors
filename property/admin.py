from django.contrib import admin

from .models import Flat, Claim, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'town', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('liked_by',)

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('author','flat',)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ['id', 'fullname', 'owner_pure_phone']
    search_fields = ['fullname']