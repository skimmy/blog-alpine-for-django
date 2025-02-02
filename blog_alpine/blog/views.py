from django.shortcuts import render

def alpine_view(request):
    context = {}
    if request.method == "POST":
            context = {
                "posted": request.POST.get("posted")
            }
    return render(request, "blog/index.html", context)