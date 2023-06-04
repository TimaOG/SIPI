var checkbox = document.getElementById('flexCheckDefaultt');
var xValues = histData.QIWI.Date;
var data1 = histData.QIWI.Close;
console.log(dataNames);
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






