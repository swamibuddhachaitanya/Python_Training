print("PATCH: request")
print("-"*20)
# ----------------
import requests

response = requests.patch("http://127.0.0.1:8000",
                         data={
                             "course": "c3",
                             "mode": "m3",
                             "location": "l3"
                         }
                         )
response = response.json()
print(response)

print("#"*40, end="\n\n")
########################################

print("GET: request after executing PATCH")
print("-"*20)
# ----------------
import requests

response = requests.get("http://127.0.0.1:8000")
response = response.json()
print(response)

print("#"*40, end="\n\n")
########################################

print("DELETE: request")
print("-"*20)
# ----------------
import requests

response = requests.delete("http://127.0.0.1:8000",
                         data={
                             "course": "c3",
                             "mode": "m3",
                             "location": "l3"

                         }
                         )
response = response.json()
print(response)

print("#"*40, end="\n\n")
########################################

print("GET: request after executing DELETE")
print("-"*20)
# ----------------
import requests

response = requests.get("http://127.0.0.1:8000")
response = response.json()
print(response)

print("#"*40, end="\n\n")
########################################