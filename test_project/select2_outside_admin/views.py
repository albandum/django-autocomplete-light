from django.views import generic
from django.core.urlresolvers import reverse_lazy

from select2_many_to_many.models import TestModel
from select2_many_to_many.forms import TestForm


class UpdateView(generic.UpdateView):
    model = TestModel
    form_class = TestForm
    template_name = 'select2_outside_admin.html'
    success_url = reverse_lazy('select2_crispy_forms')

    def get_object(self):
        return TestModel.objects.first()
