from django.contrib import admin
from .models import User, Activity,Project,Product,Client
# Register your models here.
admin.site.register(User)
admin.site.register(Activity)
admin.site.register(Project)
admin.site.register(Product)
admin.site.register(Client)