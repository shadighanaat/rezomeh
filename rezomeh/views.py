from django.shortcuts import get_object_or_404, render
from django.views import generic

from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.utils.translation import gettext as _
from django.contrib import messages
from django.utils import translation

from django.utils.translation import get_language
from django.template.loader import get_template
from django.core.mail import send_mail

from rezomeh.forms import CommentForm, ContactForm
from rezomeh.models import AboutMe, Blog, Comment, Contact, Home, Portfolio, Rezomeh
from weasyprint import HTML



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
    model = Portfolio
    template_name = 'rezomeh/portfolio_list.html'
    context_object_name = 'portfolios'
    
    def get_queryset(self):
        category = self.request.GET.get('category', 'all')
        if category == 'all':
            return Portfolio.objects.all()
        else:
            return Portfolio.objects.filter(category=category)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'rezomeh/portfolio_detail.html'
    context_object_name = 'portfolio'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

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
    

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f" {name}"
            body = f" {name}\n: {email}\n\n{message}"

            send_mail(subject, body, email, ["shadighanaati@gmail.com"])

            messages.success(request, _('Email successfully created'))

    else:
        form = ContactForm()

    return render(request, "rezomeh/contact_list.html", {"form": form})


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        blog_id = int(self.kwargs['blog_id'])
        blog = get_object_or_404(Blog, id=blog_id)
        obj.blog = blog

        parent_id = self.request.POST.get('parent_id')
        if parent_id:
            parent_comment = Comment.objects.get(id=parent_id)
            obj.parent = parent_comment  # اصلاح شده

        obj.save()

        messages.success(self.request, _('Comment successfully created'))
        return redirect('blog_detail', pk=blog.id)
    
    

def switch_language(request):
    current_language = translation.get_language()
    new_language = 'fa' if current_language == 'en' else 'en'
    translation.activate(new_language)

    next_url = request.GET.get('next', '/')

    response = redirect(next_url)
    response.set_cookie('django_language', new_language)
    request.session['django_language'] = new_language
    
    return response


def home_view(request):
    context = {
        'LANGUAGE_CODE': get_language()
    }
    return render(request, 'rezomeh.html', context)


    
def download_cv(request):
    template = get_template('rezomeh/rezomeh_list.html') 
    html = template.render({})
    pdf_file = HTML(string=html).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response


def health_check(request):
    return HttpResponse("OK")
