from django.shortcuts import render
# from django.http import HttpResponse


def home_page(request):
    return render(request, 'home.html', {
            'new_item_text': request.POST.get('item_text', ''), 
            # still should know exactly where this dict-like object lives 
            # in the object that packs all the request data
        })