from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect

from django.utils.translation import gettext as _
from django.contrib import messages
from django.utils import translation
from django.utils.translation import get_language

from rezomeh.forms import CommentForm
from rezomeh.models import AboutMe, Blog, Comment, Contact, Home, Portfolio, Rezomeh


class HomeView(generic.ListView):
    queryset = Home.objects.all()
    template_name = 'rezomeh/home_list.html'
    context_object_name = 'homes'


class AboutMeView(generic.ListView):
    queryset = AboutMe.objects.all()
    template_name = 'rezomeh/aboutme_list.html'
    context_object_name = 'aboutmes'


class RezomehView(generic.ListView):
    queryset = Rezomeh.objects.all()  
    template_name = 'rezomeh/rezomeh_list.html'  
    context_object_name = 'rezomes'


class PortfolioView(generic.ListView):
    queryset = Portfolio.objects.all()  
    template_name = 'rezomeh/portfolio_list.html'  
    context_object_name = 'portfolios'



class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'rezomeh/portfolio_detail.html'
    context_object_name = 'portfolio'


class BlogView(generic.ListView):
    queryset = Blog.objects.all()  
    template_name = 'rezomeh/blog_list.html'  
    context_object_name = 'blogs'


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'rezomeh/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    

class ContactView(generic.ListView):
    queryset = Contact.objects.all()  
    template_name = 'rezomeh/contact_list.html'  
    context_object_name = 'contacts'


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        blog_id = int(self.kwargs['blog_id'])
        blog = get_object_or_404(Blog, id=blog_id)
        obj.blog = blog

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)    
    


def switch_language(request):
    current_language = translation.get_language()
    new_language = 'fa' if current_language == 'en' else 'en'  # تغییر زبان
    translation.activate(new_language)  # فعال کردن زبان جدید
    response = redirect(request.META.get('HTTP_REFERER', '/'))  # بازگشت به صفحه قبلی
    response.set_cookie('django_language', new_language)  # ذخیره زبان جدید در کوکی
    return response


def home_view(request):
    context = {
        'LANGUAGE_CODE': get_language()
    }
    return render(request, 'your_template.html', context)
