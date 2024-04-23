from django.contrib import admin

# Register your models here.
from products.models import ProductCategory,Product,Basket


admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity','category')
    fields = ('name','description',('price','quantity'),'category','image')
    readonly_fields = ('name','description','image')
    search_fields = ('name',)
    ordering = ('name','-category')

class BasketAdmin(admin.TabularInline):
    model = Basket
    list_display=('name','quantity')