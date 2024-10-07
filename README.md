# frede_mp3.js
Mobile-API for [frede.mp3](https://play.google.com/store/apps/details?id=com.HonoLiteGames.mishkafredee) game

## Example
```JavaScript
async function main() {
	const { FredeMp3 } = require("./frede_mp3.js")
	const fredeMp3 = new FredeMp3()
	const global = await fredeMp3.getGlobal()
	console.log(global)
}

main()
```
