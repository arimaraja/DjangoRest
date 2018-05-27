from django.contrib import admin

from .models import Article,Voter,PolledInfo


# Register your models here.
admin.site.register(Article)
admin.site.register(Voter)
admin.site.register(PolledInfo)
