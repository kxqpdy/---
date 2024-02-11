import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/track/%7Bid%7D"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())