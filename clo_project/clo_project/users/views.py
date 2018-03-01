from datatableview import helpers
from datatableview import Datatable
from datatableview.views import XEditableDatatableView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from .models import BatchException, User


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

class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'

class XEditableColumnsDatatableView(XEditableDatatableView):
    template_name = "batchexception_list.html"
    model = BatchException
    class datatable_class(Datatable):
        class Meta:
            columns = ['batchExceptionID', 'batchID', 'createdBy', 'createdOn', 'modifiedBy', 'modifiedOn', 'fileName', 'exceptionReason']
            processors = {
                'batchExceptionID': helpers.make_xeditable,
                'batchID': helpers.make_xeditable,
                'createdBy': helpers.make_xeditable,
                'createdOn': helpers.make_xeditable,
                'modifiedBy': helpers.make_xeditable,
                'modifiedOn': helpers.make_xeditable,
                'fileName': helpers.make_xeditable,
                'exceptionReason': helpers.make_xeditable,
            }


"""
class BatchExceptionDatatableView(XEditableDatatableView):
    model = BatchException
    #template_name = 'users/x_editable_columns.html'
    datatable_options = {
 	'columns': [
                ('ID', 'batchExcpetionID', helpers.make_xeditable),
                ('Batch Id', 'batchID', helpers.make_xeditable),
                ('Created By', 'createdBy', helpers.make_xeditable),
                ('Created Date', 'createdOn', helpers.make_xeditable),
                ('Modified By', 'modifiedBy', helpers.make_xeditable),
                ('Modified Date', 'modifiedOn', helpers.make_xeditable),
                ('File Name', 'fileName', helpers.make_xeditable) 
        ]
    }

    implementation = u
    class BatchExceptionDatatableView(XEditableDatatableView):
        model = BatchException
        template_name = 'users/x_editable_columns.html'
        datatable_options = {
 	    'columns': [
                ('ID', 'batchExcpetionID', helpers.make_xeditable),
                ('Batch Id', 'batchID', helpers.make_xeditable),
                ('Created By', 'createdBy', helpers.make_xeditable),
                ('Created Date', 'createdOn', helpers.make_xeditable),
                ('Modified By', 'modifiedBy', helpers.make_xeditable),
                ('Modified Date', 'modifiedOn', helpers.make_xeditable),
                ('File Name', 'fileName', helpers.make_xeditable)
            ]
        }                                                                                                                                    
    </pre>                                                                                                                                         <pre class="brush: javascript">                                                                                                                // Page javascript                                                                                                                             datatableview.auto_initialize = false;                                                                                                         $(function(){                                                                                                                                      var xeditable_options = {};
             datatableview.initialize($('.datatable'), {                                                                                                   fnRowCallback: datatableview.make_xeditable(xeditable_options),                                                          
        });                                                                                                                           
    })"""
