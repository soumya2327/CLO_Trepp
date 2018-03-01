from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from datatableview.views import XEditableDatatableView
from datatableview import helpers

from .models import User,  BatchException

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)

class BatchExceptionListView(ListView):
     model = BatchException
     fields = ['batchExceptionId', 'fileName', 'exceptionReason', 'ModifiedBy']
     #slug_field = 'batchExceptionId'
     #slug_url_kwarg = 'batchExceptionId'
    
     
class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'

"""
class XEditableColumnsDatatableView(XEditableDatatableView):
    model = Entry
    datatable_options = {
 	'columns': [
                'id',
                ("Headline", 'headline', helpers.make_xeditable),
                ("Blog", 'blog', helpers.make_xeditable),
                ("Published date", 'pub_date', helpers.make_xeditable),
        ]
    }
"""
