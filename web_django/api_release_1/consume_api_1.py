"""
consume_api_1.py
"""

import requests
# response = requests.post(" http://127.0.0.1:8000/postdbdata/",
#                          data={
#                              "course": "python",
#                              "mode": "online",
#                              "location": "India"
#                          })

# response = requests.post(" http://127.0.0.1:8000/putdbdata/",
#                          data={
#                              "course": "python",
#                              "mode": "offline",
#                              "location": "India"
#                          })

# response = requests.post(" http://127.0.0.1:8000/patchdbdata/",
#                          data={
#                              "course": "python",
#                              "mode": "offline",
#                              "location": "IND"
#                          })

response = requests.post(" http://127.0.0.1:8000/deletedbdata/",
                         data={
                             "course": "python",
                             "mode": "offline",
                             "location": "IND"
                         })


response = response.json()
print(response)