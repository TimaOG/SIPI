var xValuess = ["Apple", "Apple", "Apple", "Apple", "Apple"];
var yValuess = [55, 49, 44, 24, 15];
var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart("myChartt", {
  type: "doughnut",
  data: {
    labels: xValuess,
    datasets: [{
      backgroundColor: barColors,
      data: yValuess
    }]
  },
  options: {
    title: {
      display: true,
      text: "Топ 5 акций"
    }
  }
});