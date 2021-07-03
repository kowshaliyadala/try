from django.http import HttpResponse, JsonResponse
import json
from django.shortcuts import render

def register(request):
    """
    To get some data of the user, and store it inside db.json
    """
    with open('productDB.json', 'r') as f:
        users = json.load(f)
    userData = json.loads(request.body)

    for user in users:
        if user['email'] == userData['email']:
            return JsonResponse({'status': False, 'message': 'user already exists!'})

    users.append(userData)

    # 100 users -> 105 users
    # after appending their own data -> 6

    with open('db.json', 'w') as f:
        json.dump(users, f, indent=4)

    return JsonResponse({'status': True})


def fetchUsers(request):
    print(request.method)

    """
    Send all the users data which are stored inside db.json
    """

    with open('db.json', 'r') as f:
        users = json.load(f)

    return JsonResponse({'status': True, 'users': users})



def products(request):

    with open('productDB.json', 'r') as f:
        product = json.load(f)
        return JsonResponse({'status': True, 'product': product})