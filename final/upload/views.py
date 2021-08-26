from django.shortcuts import render

# Create your views here.
def upload(request):
    if request.method == 'POST':
        radoption = request.POST['menu']
        print(radoption)
    return render(request, "upload.html")

def result(request):
    return render(request, "result.html")