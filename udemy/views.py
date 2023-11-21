from django.shortcuts import render
from django.views.generic import ListView
import pandas as pd

from courses.models import Course, Category


def index(request):
    return render(request, 'index.html', {})


class HomeListView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_courses'] = self.model.objects.all().order_by('?')
        return context


class SearchView(ListView):
    model = Course
    template_name = 'search.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(title__contains=self.request.GET['q'])



# views.py

from django.shortcuts import render

def your_view(request):
    csv_file_path = r'./web-crawler/output.csv'
    columns = ['id', 'url']


    csv_data = pd.read_csv(csv_file_path)

    # Get the top 20 rows
    top_20_data = csv_data.head(20)

    # Convert the data to a list of dictionaries for easy access in the template
    data_list = top_20_data.to_dict(orient='records')

    return render(request, 'crawler.html', {'csv_file_path': csv_file_path, 'columns': columns})


