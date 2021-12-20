from django.shortcuts import render
from .models import frontEndModel, fullStackModel, mobileDevModel
import requests

def frontend(request):
    #Search query for Frontend Developers (In the query it's as Front End Developers, because there were more results.) that are located in Turkey and have more than 10 repos
    #It only shows 30 at a time as default. You can make that 100 by adding &per_page=100 at the end of the query.
    #I left it at 30 because the more data that is saved on the database in runtime, the more time it takes to load the relevant page.
    frontend = requests.get('https://api.github.com/search/users?q=Front+End+Developer+location:Turkey+repos:>10')
    liste = []
    liste.append(frontend.json())
    cleanedData = []
    contentData = {}
    for data in liste:
        contentData['items'] = data['items']
    contentData2 = contentData['items']
    cleanedData = []
    for data in contentData2:
         cleanedData.append(data['url'])
    
    #I parsed the data twice because the data I need is in a JSON inside of a list that is inside of a JSON.
    finalver = {}
    sayac = 0
    for data in cleanedData:
        finalver[sayac] = cleanedData[sayac]
        sayac = sayac + 1

    sayac2 = 0
    for data in cleanedData:
        
        #This request provides me the details of the people that showed up on the search query
        getProf = requests.get(cleanedData[sayac2])# YOU NEED TO CHANGE THIS
        #YOU NEED TO CHANGE THE ABOVE LINE TO getProf = requests.get(cleanedData[sayac2], auth=('yourGitHubUserName','yourGitHubAPItoken'))
        sayac2=sayac2+1
        liste2 = []
        liste2.append(getProf.json())
        for data2 in liste2:
            girdi = frontEndModel()
           
            #I only save the details I need to the database. 
            girdi.html_url = data2['html_url']
            girdi.name = data2['name']
            girdi.username = data2['login']
            girdi.bio = data2['bio']
            girdi.mail = data2['email']
            girdi.avatar_url = data2['avatar_url']
            girdi.save()
    
    #I store all data base information and send it to relevant html to use 
    showall = frontEndModel.objects.all()
    return render(request, 'main.html', {'data' : showall})

#I'll only be explaining the search queries from now on because remaining parts of the functions are the same

def fullStack(request):
    #Search query for Full Stack Software Engineer that are located in Turkey
    fullStack = requests.get('https://api.github.com/search/users?q=Full+Stack+Software+Engineer+location:Turkey')
    liste = []
    liste.append(fullStack.json())
    cleanedData = []
    contentData = {}
    for data in liste:
        contentData['items'] = data['items']
    contentData2 = contentData['items']
    cleanedData = []
    for data in contentData2:
         cleanedData.append(data['url'])

    finalver = {}
    sayac = 0
    for data in cleanedData:
        finalver[sayac] = cleanedData[sayac]
        sayac = sayac + 1

    sayac2 = 0
    for data in cleanedData:
        getProf = requests.get(cleanedData[sayac2])# YOU NEED TO CHANGE THIS
        #YOU NEED TO CHANGE THE ABOVE LINE TO getProf = requests.get(cleanedData[sayac2], auth=('yourGitHubUserName','yourGitHubAPItoken'))
        sayac2=sayac2+1
        liste2 = []
        liste2.append(getProf.json())
        for data2 in liste2:
            girdi = fullStackModel()
          
            girdi.html_url = data2['html_url']
            girdi.name = data2['name']
            girdi.username = data2['login']
            girdi.bio = data2['bio']
            girdi.mail = data2['email']
            girdi.avatar_url = data2['avatar_url']
            girdi.save()

    showall = fullStackModel.objects.all()
    return render(request, 'fullStack.html', {'data' : showall})

def mobileDev(request):
    #Search query for Mobile Developers that are located in Turkey and have more than 10 repos
    mobileDev = requests.get('https://api.github.com/search/users?q=Mobile+Developer+location:Turkey+repos:>10')
    liste = []
    liste.append(mobileDev.json())
    cleanedData = []
    contentData = {}
    for data in liste:
        contentData['items'] = data['items']
    contentData2 = contentData['items']
    cleanedData = []
    for data in contentData2:
         cleanedData.append(data['url'])

    finalver = {}
    sayac = 0
    for data in cleanedData:
        finalver[sayac] = cleanedData[sayac]
        sayac = sayac + 1

    sayac2 = 0
    for data in cleanedData:
        getProf = requests.get(cleanedData[sayac2])# YOU NEED TO CHANGE THIS
        #YOU NEED TO CHANGE THE ABOVE LINE TO getProf = requests.get(cleanedData[sayac2], auth=('yourGitHubUserName','yourGitHubAPItoken'))
        sayac2=sayac2+1
        liste2 = []
        liste2.append(getProf.json())
        for data2 in liste2:
            girdi = mobileDevModel()
          
            girdi.html_url = data2['html_url']
            girdi.name = data2['name']
            girdi.username = data2['login']
            girdi.bio = data2['bio']
            girdi.mail = data2['email']
            girdi.avatar_url = data2['avatar_url']
            girdi.save()

    showall = mobileDevModel.objects.all()
    return render(request, 'mobileDev.html', {'data' : showall})
