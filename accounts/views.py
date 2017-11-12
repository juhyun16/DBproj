from django.shortcuts import render
from django.db import connection

# Create your views here.

def login(request):
    context = dict()

    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM sadmin''')
    row = cursor.fetchone()

    context["ID"] = row[1]
    context["PW"] = row[2]
    return render(request, "home.html", context)


