import django_tables2 as tables

from .models import Studies


class StudiesTable(tables.Table):

    class Meta:
        model = Studies
