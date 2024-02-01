"""
Access rest api using requests library
"""
import requests

print("Testing API with: GET Request")
print("-"*20)
# ---------------

try:
    api_response = requests.get("http://127.0.0.1:5000/getdata")
    api_response = api_response.json()
    print(api_response)
except:
    print("Not able to access API, Please make sure to run my_rest_api_release.py")

print("#"*40, end="\n\n")
###############################

print("Testing API with: POST Request")
print("-"*20)
# ---------------

try:
    api_response = requests.post("http://127.0.0.1:5000/postdata",
                                 json={'course_id': 3, 'course_location': 'l3', 'course_mode': 'm3', 'course_name': 'n3'}
                                 )
    api_response = api_response.json()
    print(api_response)
except:
    print("Not able to access API, Please make sure to run my_rest_api_release.py")

print("#"*40, end="\n\n")
###############################

print("Testing API with: PUT Request")
print("-"*20)
# ---------------

try:
    api_response = requests.put("http://127.0.0.1:5000/putdata",
                                 json={'course_id': 4, 'course_location': 'lll3', 'course_mode': 'm3', 'course_name': 'n3'}
                                 )
    api_response = api_response.json()
    print(api_response)
except:
    print("Not able to access API, Please make sure to run my_rest_api_release.py")

print("#"*40, end="\n\n")
###############################

print("Testing API with: GET Request After Update")
print("-"*20)
# ---------------

try:
    api_response = requests.get("http://127.0.0.1:5000/getdata")
    api_response = api_response.json()
    print(api_response)
except:
    print("Not able to access API, Please make sure to run my_rest_api_release.py")

print("#"*40, end="\n\n")
###############################

print("Testing API with: PATCH Request")
print("-"*20)
# ---------------

try:
    api_response = requests.patch("http://127.0.0.1:5000/patchdata",
                                 json={'course_id': 14, 'course_location': 'lll3', 'course_mode': 'm3', 'course_name': 'n3'}
                                 )
    api_response = api_response.json()
    print(api_response)
except:
    print("Not able to access API, Please make sure to run my_rest_api_release.py")

print("#"*40, end="\n\n")
###############################

print("Testing API with: GET Request After PATCH")
print("-"*20)
# ---------------

try:
    api_response = requests.get("http://127.0.0.1:5000/getdata")
    api_response = api_response.json()
    print(api_response)
except:
    print("Not able to access API, Please make sure to run my_rest_api_release.py")

print("#"*40, end="\n\n")
###############################


print("Testing API with: DELETE Request")
print("-"*20)
# ---------------

try:
    api_response = requests.delete("http://127.0.0.1:5000/deletedata",
                                 json={'course_id': 14, 'course_location': 'lll3', 'course_mode': 'm3', 'course_name': 'n3'}
                                 )
    api_response = api_response.json()
    print(api_response)
except:
    print("Not able to access API, Please make sure to run my_rest_api_release.py")

print("#"*40, end="\n\n")
###############################

print("Testing API with: GET Request After DELETE")
print("-"*20)
# ---------------

try:
    api_response = requests.get("http://127.0.0.1:5000/deletedata")
    api_response = api_response.json()
    print(api_response)
except:
    print("Not able to access API, Please make sure to run my_rest_api_release.py")

print("#"*40, end="\n\n")
###############################