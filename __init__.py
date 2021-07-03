from django.http import HttpResponse, JsonResponse
import json


def gmail_login(request):
    return HttpResponse("This is the gmail-login")


def linkedin_login(request):
    dictionary = {'message': 'This is the linkedin-login'}
    string = json.dumps(dictionary)
    return HttpResponse(string)


def register(request):
    """
    To get some data of the user, and store it inside db.json
    """
    with open('db.json', 'r') as f:
        users = json.load(f)
        userData = json.loads(request.body)
        print(request.body)
    for user in users:
        if user['email'] == userData['email']:
            return JsonResponse({'status': False, 'message': 'user already exists!'})

    users.append(userData)

    # 100 users -> 105 users
    # after appending their own data -> 6

    with open('db.json', 'w') as f:
        json.dump(users, f, indent=4)

    return JsonResponse({'status': True})


def fetchUser(request):
    """
    to send the data
    """
    with open('db.json', 'r') as f:
        users = json.load(f)
    return JsonResponse({'status': True, 'users': users})