from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

def home(request, year, month):
    name = "Greg"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create a Calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)

    return render(request, 'home.html', {
        "name":name,
        "year":year,
        "month":month,
        "month_number":month_number,
        "cal":cal,
    })

