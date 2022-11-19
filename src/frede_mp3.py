import requests

class FredeMP3:
	def __init__(self) -> None:
		self.api = "https://fredemp3.ru/S3RATE228"
		self.headers = {
			"user-agent": "UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)",
			"x-unity-version": "2021.3.8f1"
		}

	def login(self, username: str, password: str) -> str:
		data = {
			"loginUser": username,
			"loginPassword": password
		}
		return requests.post(
			f"{self.api}/Login.php",
			data=data,
			headers=self.headers).text

	def get_global(self) -> str:
		return requests.get(
			f"{self.api}/getGlobal.php",
			headers=self.headers).text

	def register(
			self,
			username: str,
			password: str,
			email: str) -> str:
		data = {
			"loginUser": username,
			"loginPassword": password,
			"email": email
		}
		return requests.post(
			f"{self.api}/Register.php",
			data=data,
			headers=self.headers).text

	def save_other(
			self,
			username: str,
			statistics: list,
			values: list) -> str:
		data = {
			"loginUser": username
		}
		data.update(dict(zip(statistics, values)))
		return requests.post(
			f"{self.api}/saveOther.php",
			data=data,
			headers=self.headers).text

	def save_cards(
			self,
			username: str,
			cards: list,
			value: int) -> str:
		data = {
			"loginUser": username
		}
		for card in cards:
			data[card] = value
		return requests.post(
			f"{self.api}/saveCards.php",
			data=data,
			headers=self.headers).text

	def get_other(self, username: str) -> str:
		data = {
			"loginUser": username
		}
		return requests.post(
			f"{self.api}/getOther.php",
			data=data,
			headers=self.headers).text
