from .models import Language
def getLanguages(request):
    languages=Language.objects.all()
    return locals()