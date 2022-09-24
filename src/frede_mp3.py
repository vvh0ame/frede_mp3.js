import requests

class FredeMP3:
	def __init__(self):
		self.api = "https://fredemp3.ru"
		self.headers = {
			"user-agent": "UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)",
			"x-unity-version": "2021.3.8f1"
		}

	def login(self, username: str, password: str):
		data = {
			"loginUser": username,
			"loginPassword": password
		}
		return requests.post(
			f"{self.api}/S3RATE228/Login.php",
			data=data,
			headers=self.headers).text

	def get_global(self):
		return requests.get(
			f"{self.api}/S3RATE228/getGlobal.php",
			headers=self.headers).text

	def register(
			self,
			username: str,
			password: str,
			email: str):
		data = {
			"loginUser": username,
			"loginPassword": password,
			"email": email
		}
		return requests.post(
			f"{self.api}/S3RATE228/Register.php",
			data=data,
			headers=self.headers).text

	def save_other(
			self,
			username: str,
			statistics: list,
			values: list):
		data = {
			"loginUser": username
		}
		for statistic in statistics:
			for value in values:
				data[statistic] = value
		return requests.post(
			f"{self.api}/S3RATE228/saveOther.php",
			data=data,
			headers=self.headers).text

	def save_cards(
			self,
			username: str,
			cards: list,
			value: int):
		data = {
			"loginUser": username
		}
		for card in cards:
			data[card] = value
		return requests.post(
			f"{self.api}/saveCards.php",
			data=data,
			headers=self.headers).text

	def get_other(self, username: str):
		data = {
			"loginUser": username
		}
		return requests.post(
			f"{self.api}/S3RATE228/getOther.php",
			data=data,
			headers=self.headers).text
