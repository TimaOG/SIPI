var list = new Map;
var chartOptions;
var checkbox;
var current_id;
var current_name;


//function getChart() {
//    current_id = id;
//    current_name = name;
//    list.set(current_id, histData[name]['Close'])
//    checkbox = document.getElementById(`flexCheckDefault_${name}`);
//    chartOptions = {
//        type: "line",
//        data: {
//            labels: histData[name]['Date'],
//            datasets: [
//                {
//                    data: checkbox.checked ? list.get(current_id) : [],
//                    borderColor: "red",
//                    fill: false
//                }
//            ]
//        },
//        options: {
//            legend: {display: false}
//        }
//    }
//    //checkbox.addEventListener('change', function () {
//    // });
//}
function getChart() {
    var stock = document.getElementsByClassName("checkBoxStock")
    var dataset = []
    for(var i = 0; i < stock.length; i++) {
        if(stock[i].checked) {
            dataset.push({
                data: histData[stock[i].name]['Close'],
                borderColor: "red",
                fill: false
            })
        }
    }
    chartOptions = {
        type: "line",
        data: {
            labels: histData[name]['Date'],
            datasets: dataset
        },
        options: {
            legend: {display: false}
        }
    }
    var chart = new Chart("myCharttt", chartOptions);
    chart.update();
}

//var chart = new Chart("myCharttt", chartOptions);
//checkbox.addEventListener('change', function () {
//    chart.data.datasets[current_id].data = this.checked ? list.get(current_id) : [];
//    chart.update();
//});
//// if (checkbox) {
////     checkbox.addEventListener('change', function () {
////         chart.options = chartOptions;
////         console.log(chartOptions);
////         chart.update();
////     });
////     console.log(current_id, list.get(current_id));
//// }







