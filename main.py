import subprocess
import requests

subprocess = subprocess.Popen("py transcribe.py audio.mp3", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
print(subprocess_return)


# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
# payload = f"q={subprocess_return}&target=nl&source=en"
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"Accept-Encoding": "application/gzip",
# 	"X-RapidAPI-Key": "2004ffae2bmsh309f8dddc1feca4p181963jsne3b1df7d9baa",
# 	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
# }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)