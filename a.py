from decouple import config

API_USERNAME = config('USER')

print(API_USERNAME)