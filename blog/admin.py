from django.contrib import admin
from .models import Post
from .models import FizykaPost
from .models import InfaPost

admin.site.register(Post)
admin.site.register(FizykaPost)
admin.site.register(InfaPost)
