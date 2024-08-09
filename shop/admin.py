from django.contrib import admin
from . models import *

# Register your models here.



class catagoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
    
admin.site.register(category,catagoryAdmin)

class productAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug','price','stock','image']
    list_editable=['price','stock','image']
admin.site.register(products,productAdmin)
