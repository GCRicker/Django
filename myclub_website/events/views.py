from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Greg"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create a Calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)

    return render(request, 'events/home.html', {
        "name":name,
        "year":year,
        "month":month,
        "month_number":month_number,
        "cal":cal,
    })

