class FredeMp3 {
	constructor() {
		this.api = "https://fredemp3.ru/S3RATE228"
		this.headers = {
			"user-agent": "UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)",
			"x-unity-version": "2021.3.8f1"
		}
	}

	async login(userName, password) {
		const response = await fetch(
			`${this.api}/login.php`, {
				method: "POST",
				body: JSON.stringify({
					loginUser: userName,
					loginPassword: password
				}),
				headers: this.headers
			})
		return response.text()
	}

	async register(userName, password, email) {
		const response = await fetch(
			`${this.api}/Register.php`, {
				method: "POST",
				body: JSON.stringify({
					loginUser: userName,
					loginPassword: password,
					email: email
				}),
				headers: this.headers
			})
		return response.text()
	}

	async getGlobal() {
		const response = await fetch(
			`${this.api}/getGlobal.php`, {
				method: "GET",
				headers: this.headers
			})
		return response.text()
	}

	async saveOther(userName, statistics, values) {
		const body = {
			loginUser: userName,
		}
		statistics.forEach((stat, index) => {
			body[stat] = values[index];
		})
		const response = await fetch(
			`${this.api}/saveOther.php`, {
				method: "POST",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.text()
	}

	async saveCards(userName, cards, value) {
		const body = {
			loginUser: userName,
		}
		cards.forEach(card => {
			body[card] = value;
		})
		const response = await fetch(
			`${this.api}/saveCards.php`, {
				method: "POST",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.text()
	}

	async getOther(userName) {
		const response = await fetch(
			`${this.api}/getOther.php`, {
				method: "POST",
				body: JSON.stringify({
					loginUser: userName
				}),
				headers: this.headers
			})
		return response.text()
	}
}

module.exports = {FredeMp3}
