const api ='api.openweathermap.org/data/2.5/weather';
const city='Dodoma';
const country='tz';
const appid='d3243a8091f7937403f8541ce92c32c8';

fetch("https://"+ api +"?q="+ city +","+ country +" &appid="+ appid)
	.then(response => response.json())
	.then(data => {
		document.getElementById('temp').innerHTML=data.main.temp;
		document.getElementById('temp-min').innerHTML=data.main.temp_min;
		document.getElementById('temp-max').innerHTML=data.main.temp_max;
		document.getElementById('wind.speed').innerHTML=data.wind.speed;
		document.getElementById('wind.direction').innerHTML=data.wind.deg;
		document.getElementById('clouds').innerHTML=data.clouds.all;
		document.getElementById('humidity').innerHTML=data.main.humidity;
		document.getElementById('city').innerHTML=data.name;
		document.getElementById('country').innerHTML=data.sys.country;
	})