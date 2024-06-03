from django.shortcuts import render, redirect

from mysite.models import SubscriberForm


def home(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("success")

    else:
        form = SubscriberForm()


    context = {
        "content": "Sign up to the newsletter", 
        "form": form, 
    }

    return render(request, "home.html", context)


def success(request):
    context = {
        "content": "Thanks for signing up to the newsletter!",
    }
    return render(request, "home.html", context)
