
const apikey ="ba7631cf13d6729105021e3f9a4b85f7";
const apiUrl="https://api.openweathermap.org/data/2.5/weather?&units=metric&q=";
const searchBox=document.querySelector(".search input")
const searchBtn=document.querySelector(".search button")
const wether_icon = document.querySelector(".wether_icon")
async function checkWeather(city){
const response=await fetch(apiUrl +city + `&appid=${apikey}`);
var data = await response.json();
console.log(data)
document.querySelector(".city").innerHTML= data.name;
document.querySelector(".temp").innerHTML= Math.round(data.main.temp) +"°c";
document.querySelector(".humidity").innerHTML= data.main.humidity +"%";
document.querySelector(".wind").innerHTML= data.wind.speed + "km/h";
if (data.weather [0].main =="Clouds"){
    wether_icon.src="AGIT/image/clouds.png";
}
else if (data.weather [0].main =="Clear"){
    wether_icon.src="AGIT/image/Clear.png";} 
else if (data.weather [0].main =="Rain"){
    wether_icon.src="AGIT/image/rain.png";} 
else if (data.weather [0].main =="Drizzle"){
    wether_icon.src="AGIT/image/drizzle.png";}  
else if (data.weather [0].main =="Mist"){
    wether_icon.src="AGIT/image/mist.png";}         
}
searchBtn.addEventListener("click",()=>{
checkWeather(searchBox.value);
})

/*const x = document.getElementById("demo");*/
const data = {
    labels: ['January', 'February', 'March', 'April', 'May'],
    datasets: [{
      label: 'Sales',
      data: [50, 60, 70, 65, 80],
      backgroundColor: 'rgba(255, 99, 132, 0.5)', // Change bar color
      borderColor: 'rgba(255, 99, 132, 1)', // Change bar border color
      borderWidth: 2 // Change bar border width
    }]
  };

  // Configuration options
  const options = {
    responsive: false, // Set responsive to false
    maintainAspectRatio: true, // Maintain aspect ratio
    aspectRatio: 1, // Set aspect ratio to 1:1 (square)
    scales: {
      y: {
        beginAtZero: true,
        // Change y-axis color
        grid: {
          color: 'rgba(0, 0, 0, 0.1)' // Change grid color
        }
      },
      x: {
        // Change x-axis color
        grid: {
          color: 'rgba(0, 0, 0, 0.1)' // Change grid color
        }
      }
    },
    plugins: {
      legend: {
        labels: {
          // Change legend font color
          color: 'black'
        }
      }
    }
  };

  // Create the chart
  const ctx = document.getElementById('myChart').getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: options
  });
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            showPosition(latitude, longitude); // Call showPosition with latitude and longitude
        });
    } else {
        /*x.innerHTML = "Geolocation is not supported by this browser.";*/
    }
}

getLocation(); // Call getLocation to get the current position

function showPosition(latitude, longitude) {
    /*x.innerHTML = "Latitude: " + latitude + "<br>Longitude: " + longitude;*/
    init(latitude, longitude); // Call init with latitude and longitude
}

function init(latitude, longitude) {
    const map = new ol.Map({
        view: new ol.View({
            center: ol.proj.fromLonLat([longitude, latitude]),
            zoom: 10
        }),
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        target: 'js-map'
    });
}