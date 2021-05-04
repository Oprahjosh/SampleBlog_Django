from django.contrib import admin
#from .models import Post, Accounts

# Register your models here.
from myBlog.models import Post
#from Blog.register.models import Register1

admin.site.register(Post)
#admin.site.register(Register1)

'''@admin.register(Accounts)
class AccountAdmin(admin.ModelAdmin):
    pass
'''
