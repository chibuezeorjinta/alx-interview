#!/usr/bin/node

const request = require('request');
const filmNum = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + filmNum + '/';

const getCharacterList = () => {
	request(url, async function (err, response, body) {
		if (err) return console.log('Fetch Error For Character URL');

		const characterList = JSON.parse(body).characters;

		const outChareList = []
		for (const chUrl of characterList) {
			let outChara = new Promise((resolve, reject) => {
				request(chUrl, (err, response, body) => {
					if (err) return console.log('Fetch Error For Character Data');
					resolve(JSON.parse(body).name);
				})
			})
			outChareList.push(outChara);
		}

		const data = await Promise.all(outChareList);
		for (const name of data) {
			console.log(name)
		}
	});
}

getCharacterList(url);