from django.http import HttpResponse
from django.template import loader

from .models import Member

# Create your views here.

# def members(request):
#     template = loader.get_template('sample.html')
#     return HttpResponse(template.render())

def members(request):
  mymembers = Member.objects.all().values() #fetching data
  template = loader.get_template('displaymembers.html')  #loading the template
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  print("mymember-->",str(mymember))
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def addusers(request):
  mymember1 = Member(firstname='Tarun', lastname='Yadav', phone= 7898789874)
  mymember2 = Member(firstname='Umesh', lastname='Gere')
  mymember3 = Member(firstname='Prakash', lastname='Thurman')
  mymember4 = Member(firstname='Joey', lastname='Bing')
  members_list = [mymember1, mymember2, mymember3, mymember4]
  for x in members_list:
    x.save()
  return HttpResponse("All users are saved to the DB",request)

def deleteusers(request):
  mymembers = Member.objects.all()
  mymembers.delete()
  return HttpResponse("deleted",request)

def test(request):
  mytemplate = loader.get_template('variables.html')
  context = {
    "logged_in": True,
    "manager": "Rahul",
    "users": Member.objects.all().values()
  }
  return HttpResponse(mytemplate.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# def test(request):
#   template = loader.get_template('template.html')
#   mymembers = Member.objects.all().values()
#   context = {
#     'firstname': 'Rahul',
#     'mymembers': mymembers,
#     'greeting': 1,
#     'fruits': ['apple', 'mango','banana','orange']
#   }
#   return HttpResponse(template.render(context, request))

