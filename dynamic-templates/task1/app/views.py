import csv
from app.settings import BASE_DIR

from django.shortcuts import render


def try_float(v):
    try:
        return int(v) if float(v).is_integer() else float(v)
    except ValueError:
        return None


def inflation_view(request):
    template_name = 'inflation.html'

    csv.register_dialect('custom_scv', delimiter=';', quoting=csv.QUOTE_NONE)

    with open(f"{BASE_DIR}\\inflation_russia.csv", newline='', encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, dialect='custom_scv')
        headers = reader.fieldnames
        content = []
        for row in reader:
            formatted_values = [try_float(item) for item in row.values()]
            content.append(formatted_values)

    context = {'data': content, 'headers': headers}
    return render(request, template_name, context)
