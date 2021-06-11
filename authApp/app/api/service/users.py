import os
import httpx




# Checks if user is present by calling the user-service api get_all endpoint
def is_user_present(user_type: str):

  USER_SERVICE_HOST_URL = f'http://user-service:8000/{user_type}/get_all'
  url = os.environ.get('USER_SERVICE_HOST_URL') or USER_SERVICE_HOST_URL

  try:
    r = httpx.get(f'{url}')
    return r.json() if r.status_code == 200 else r.status_code
    
  except httpx.TimeoutException as t:
    print("[X] TIMEOUT REQUEST TOOK TOO LONG TO RESPOND")
    return t
  except httpx.RequestError as r:
    print("[X] REQUEST FAILED")
    return r


# h = is_user_present("tenants")
# for val in h:
#   print(val["email"])



# get login details fom the login endpoint

