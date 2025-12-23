from django.contrib import admin
# from .models import Book, Category, Writer
# Register your models here.

# admin.site.register(Category)
# admin.site.register(Writer)

class BookAdmin(admin.ModelAdmin):
    # list view
    search_fields = ['title']
    list_display = ['title', 'price', 'rate', 'writer']
    list_filter = ['language']
    list_editable = ['price']
    

    # detail view

    # readonly_fields = ['rate']

    # exclude = ['publisher']

    fieldsets = [
        (
            "اطلاعات کتاب ",
            {
                "fields": ["title", "description"],
            },
        ),
        (
            "اطلاعات ناشر",
            {
                
                "fields": ["publisher", 'price', "rate"],
            },
        ),
        (
            "باقی",
            {
                
                "fields": ["writer", "categories"],
            },
        ),
    ]



    pass

# admin.site.register(Book, BookAdmin)



from .models import Product, ProductFeature, Comment, Person


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']

    list_filter = ['size']
    pass
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductFeature)
admin.site.register(Comment)
admin.site.register(Person)
