from django.shortcuts import render, redirect
from .models import Receipe

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_img = request.FILES.get('receipe_img')
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')
        
        print(receipe_name)
        print(receipe_desc)
        print(receipe_img)

        # Create the recipe object only if all data is available
        if receipe_img and receipe_name and receipe_desc:
            Receipe.objects.create(
                receipe_img=receipe_img,
                receipe_desc=receipe_desc,
                receipe_name=receipe_name,
            )
            return redirect('/success/')  # Assuming you have defined this URL pattern

    return render(request, 'receipe.html')
