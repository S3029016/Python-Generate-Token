import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

username = input("please provide your username:")
password = getpass("please enter your password:")


url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic RGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
