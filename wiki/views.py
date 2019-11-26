from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from wiki.forms import PageForm

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from wiki.models import Page


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page 

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

# books/views.py
class PageCreateView(CreateView):
  def get(self, request, *args, **kwargs):
      context = {'form': PageForm()}
      return render(request, 'new_wiki.html', context)

  def post(self, request, *args, **kwargs):
      form = PageForm(request.POST)
      if form.is_valid():
          wiki = form.save()
          wiki.save()
          return HttpResponseRedirect(reverse_lazy('wiki-details-page', args=[wiki.slug]))
      return render(request, 'new_wiki.html', {'form': form})

      
