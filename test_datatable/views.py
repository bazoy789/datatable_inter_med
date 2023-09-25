
from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import Studies
import random
from datetime import timedelta

from .table import StudiesTable


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def init_db(request):
    stud = Studies.objects.all()
    page_obj = StudiesTable(stud)
    RequestConfig(request, paginate={"per_page": 100}).configure(page_obj)
    search_name = request.GET.get('search')
    head = request.GET.get('select')
    mod = Studies._meta.get_fields()

    if search_name and head:
        for i in mod:
            if i.verbose_name == head:
                r = f'{i.name}__icontains'
                stud = stud.filter(**{r:search_name})
                page_obj = StudiesTable(stud)
                RequestConfig(request, paginate={"per_page": 20}).configure(page_obj)

    return render(request, 'test_datatable/init_db.html', {"page_obj": page_obj,
                                                           "mod": mod,
                                                           "search_name": search_name})
