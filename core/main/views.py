from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import HomeProduct, HomeSlide

# Քանի, որ 1 էջի վրա կարող է լինել մի քանի class պահում ենք 1 listviews ում
# Index html ի մեջ for եմ գրել 2 անգամ, 1 անգամ slide-ի վրա 2 անգամ prod-ի վրա
# Ու կայքի ամեն հատվածում ցույց եմ տվել իրա info֊ն
class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        prod = HomeProduct.objects.filter()
        slide = HomeSlide.objects.all()
        return render(request, self.template_name, {'prod':prod, 'slide':slide})

