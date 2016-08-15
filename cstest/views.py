from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from cstest.forms import testform

def test(request):
    #print request.method
    if request.method == "POST":
        print request.POST['vmid']
        print request.POST['vmstate']
        return HttpResponse("Success")
    else:
        form = testform(initial = {'vmid': 'VM UUID'})
    return render(request, 'test_form.html', {'form': form})
    #return HttpResponse("Test")
