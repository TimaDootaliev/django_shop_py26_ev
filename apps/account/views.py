from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


@api_view(['GET'])
def activate_account(request, uid, token):
    print(uid, token)
    protocol = 'https://' if request.is_secure() else 'http://'
    web_url = protocol + request.get_host()
    post_url = web_url + "/auth/users/activate/"
    post_data = {'uid': uid, 'token': token}
    result = requests.post(post_url, data = post_data)
    content = result.text
    return Response(content, status=result.status_code)