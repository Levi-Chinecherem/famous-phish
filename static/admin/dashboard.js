// dashboard.js

// Function to create and render a chart
function createChart(chartId, chartType, labels, data) {
    const ctx = document.getElementById(chartId).getContext('2d');
    new Chart(ctx, {
        type: chartType,
        data: {
            labels: labels,
            datasets: [{
                label: 'Count',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(153, 102, 255, 1)',
                ],
                borderWidth: 1,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 1000, // Set animation duration (in milliseconds)
            },
        },
    });
}

// Call createChart for each chart with the appropriate data
createChart('chart1', 'bar', {{ chart1_labels|safe }}, {{ chart1_values|safe }});
createChart('chart2', 'bar', {{ chart2_labels|safe }}, {{ chart2_values|safe }});
createChart('chart3', 'pie', {{ chart3_labels|safe }}, {{ chart3_values|safe }});
