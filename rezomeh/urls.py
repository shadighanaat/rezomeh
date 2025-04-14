from django.urls import path

from .views import (AboutMeView, 
                    BlogDetailView, 
                    BlogView, 
                    CommentCreateView,  
                    HomeView, 
                    PortfolioDetailView, 
                    PortfolioView, 
                    RezomehView,
                    contact_view,
                    switch_language,
                    download_cv,
                   
                    )
handler500 = "rezomeh.views.custom_server_error"

urlpatterns =  [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeView.as_view(), name='home_list'),
    path('aboutme/', AboutMeView.as_view(), name='aboutme_list'),
    path('rezome/', RezomehView.as_view(), name='rezomeh_list'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio_list'),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('blog/', BlogView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:blog_id>/comment', CommentCreateView.as_view(), name='comment_create'),
    path("contact/", contact_view, name="contact_list"),
    path('language/', switch_language, name='language'),
    path('download-cv/', download_cv, name='download_cv'),
    ]