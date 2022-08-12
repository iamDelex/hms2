from hotel.models import *


def dropdown(request):
    varieties = Variety.objects.all()
    
    context = {
    'varieties':varieties
    }
    return context

#this is the numbers that shows the item added to your cart