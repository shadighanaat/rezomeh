from django.urls import path

from .views import (AboutMeView, 
                    BlogDetailView, 
                    BlogView, 
                    CommentCreateView, 
                    ContactView, 
                    HomeView, 
                    PortfolioDetailView, 
                    PortfolioView, 
                    RezomehView, switch_language
                    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeView.as_view(), name='home_list'),
    path('aboutme/', AboutMeView.as_view(), name='aboutme_list'),
    path('rezomeh/', RezomehView.as_view(), name='rezomeh_list'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio_list'),
    path('<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('blog/', BlogView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
    path('contact/', ContactView.as_view(), name='contact_list'),
    path('language/', switch_language, name='language'),
    ]