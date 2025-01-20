from django.contrib import admin
from .models import (AboutMe, Blog, Category, Comment, Contact, Home, Portfolio, Rezomeh, Servise)


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['message', 'author',]
    extra = 1

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'freelance_status', ]


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['title', ]



@admin.register(Servise)
class ServiseAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', ]


@admin.register(Rezomeh)
class RezomehAdmin(admin.ModelAdmin):
    list_display = ['title', ] 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]      


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'technology', ]       


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'technology', 'author', ] 

    inlines = [
        CommentsInline,
    ]
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['message', 'author', 'blog', ]   



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'message', 'phone_number', 'email', ]      

