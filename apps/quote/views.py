"""
Quote views with HTMX form submission.
"""
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import QuoteForm


class QuoteView(CreateView):
    form_class = QuoteForm
    template_name = 'quote/quote.html'

    def form_valid(self, form):
        form.save()
        if self.request.headers.get('HX-Request'):
            return HttpResponse(
                '<div class="bg-emerald-500/20 border border-emerald-500 text-emerald-300 '
                'rounded-xl p-6 text-center">'
                '<svg class="w-12 h-12 mx-auto mb-3 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">'
                '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>'
                '</svg>'
                '<h3 class="text-lg font-bold mb-2">سفارش شما با موفقیت ثبت شد!</h3>'
                '<p class="text-sm opacity-80">کارشناسان ما به زودی با شما تماس خواهند گرفت.</p>'
                '</div>'
            )
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_invalid(form)
