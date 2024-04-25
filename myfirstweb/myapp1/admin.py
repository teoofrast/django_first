from django.contrib import admin
from myapp1.models import Product, Buyer, Cart, CartItem
from django.utils.html import format_html


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "nickname", "email")
    list_display_links = ("id", "name", "nickname")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity")
    list_display_links = ("id", "cart")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name_colored", "price", "quantity_available", "is_available")
    list_display_links = ("id", "name_colored")
    list_filter = ("quantity_available", "is_available")
    # list_per_page = 2
    search_fields = ("name",)

    def name_colored(self, obj):
        if obj.quantity_available > 5:
            color_code = "008080"
        elif obj.quantity_available == 0:
            color_code = "800000"
        else:
            color_code = "D2691E"
        html = '<span style="color: #{};">{}</span>'.format(color_code, obj.name)
        return format_html(html)

    name_colored.admin_order_field = "name"
    name_colored.short_description = "name color"


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("buyer", "display_products")
