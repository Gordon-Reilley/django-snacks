from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/LD-Fudge-Round.jpg/470px-LD-Fudge-Round.jpg",
                "title": "Fudge Rounds",
                "description": "Fudge Rounds are fudgy, round snack cakes made by Little Debbie. They are made by gluing two chewy chocolate cookies together with a light brown fudge creme. Finally, the two cookies are striped with light brown fudge.",
                "reference_url": "https://en.wikipedia.org/wiki/Fudge_Rounds"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Cheez-It-Crackers.jpg/500px-Cheez-It-Crackers.jpg",
                "title": "Cheez-Its",
                "description": "Cheez-It crackers are 26-by-24-millimetre (1.0 by 0.94 in) rectangles, though they are often believed to be squares. Cheez-It crackers are made with actual cheese, and are marketed by Kellogg's as such.",
                "reference_url": "https://en.wikipedia.org/wiki/Cheez-It"
            },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'