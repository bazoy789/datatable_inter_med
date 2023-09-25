from django_filters import FilterSet
from .models import Studies


class StudiesFilter(FilterSet):
    class Meta:
        model = Studies
        fields = {"patient_fio": ["exact", "contains"], "patient_birthdate": ["exact"]}
