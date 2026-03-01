from django.views.generic import TemplateView
from .models import AboutContent, PlusAbout, BlogAbout, Faq, Testimonials


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["about"] = AboutContent.objects.first()
        context["pluses"] = PlusAbout.objects.all()
        context["blogs"] = BlogAbout.objects.all()
        context["faqs"] = Faq.objects.all()
        context["testimonials"] = Testimonials.objects.all()

        return context