var chartOptions;

function getChart() {
    var stock = document.getElementsByClassName("checkBoxStock")
    var dataset = [];
    var colors = ["red", "green", "blue", "yellow", "purple", "black"];
    for(var i = 0; i < stock.length; i++) {
        if(stock[i].checked) {
            dataset.push({
                data: histData[stock[i].name]['Close'],
                borderColor: colors[i],
                fill: false
            })
        }
    }
    console.log(dataset);
    chartOptions = {
        type: "line",
        data: {
            labels: histData[stock[0].name]['Date'],
            datasets: dataset,
        },
        options: {
            legend: {display: false}
        }
    }
    var chart = new Chart("myCharttt", chartOptions);
    chart.update();
}







