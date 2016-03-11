from django.views.generic import TemplateView
from smyt.models import Spare
from technic.models import Technic
class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        ctx = super(MainView, self).get_context_data(**kwargs)
        ctx['spares'] = Spare.objects.order_by('name')
        ctx['technics'] = Technic.objects.order_by('name')
        return ctx
