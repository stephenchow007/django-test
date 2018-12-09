from django.contrib import admin

# Register your models here.
from TestModel.models import Author

admin.site.register(Author)