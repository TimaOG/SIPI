var checkbox = document.getElementById('flexCheckDefaultt');
var xValues = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"];
var data1 = [860, 1140, 1060, 1060, 1070, 1110, 1330, 2210, 7830, 2478];

var chartOptions = {
  type: "line",
  data: {
    labels: xValues,
    datasets: [
      { 
        data: checkbox.checked ? data1 : [],
        borderColor: "red",
        fill: false
      }
    ]
  },
  options: {
    legend: { display: false }
  }
};

var chart = new Chart("myCharttt", chartOptions);

checkbox.addEventListener('change', function() {
  chart.data.datasets[0].data = this.checked ? data1 : [];
  chart.update();
});






