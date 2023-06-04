// var checkbox = document.getElementById('flexCheckDefault_{{stock.code}}');
// var xValues = histData.QIWI.Date;
// var data1 = histData.QIWI.Close;
// console.log(dataNames);
// var chartOptions = {
//     type: "line",
//     data: {
//         labels: xValues,
//         datasets: [
//             {
//                 data: checkbox.checked ? data1 : [],
//                 borderColor: "red",
//                 fill: false
//             }
//         ]
//     },
//     options: {
//         legend: {display: false}
//     }
// };

// var chart = new Chart("myCharttt", chartOptions);
//
// checkbox.addEventListener('change', function () {
//     chart.data.datasets[0].data = this.checked ? data1 : [];
//     chart.update();
// });

var list = new Map;
var chartOptions;
var checkbox;
var current_id;
var current_name;


function getChart(name, id) {
    current_id = id;
    current_name = name;
    list.set(current_id, histData[name]['Close'])
    checkbox = document.getElementById(`flexCheckDefault_${name}`);
    chartOptions = {
        type: "line",
        data: {
            labels: histData[name]['Date'],
            datasets: [
                {
                    data: checkbox.checked ? list.get(current_id) : [],
                    borderColor: "red",
                    fill: false
                }
            ]
        },
        options: {
            legend: {display: false}
        }
    }
    //checkbox.addEventListener('change', function () {
    // });
}

var chart = new Chart("myCharttt", chartOptions);
checkbox.addEventListener('change', function () {
    chart.data.datasets[current_id].data = this.checked ? list.get(current_id) : [];
    chart.update();
});
// if (checkbox) {
//     checkbox.addEventListener('change', function () {
//         chart.options = chartOptions;
//         console.log(chartOptions);
//         chart.update();
//     });
//     console.log(current_id, list.get(current_id));
// }







