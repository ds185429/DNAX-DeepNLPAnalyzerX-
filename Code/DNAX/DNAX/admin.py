from django.contrib import admin
from .models  import *

# Register your models here.
admin.site.site_header="NCR Administration"
admin.site.register(Users)
admin.site.register(ConfigFiles)