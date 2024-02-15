import {
  Chart,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from 'chart.js';
import { Scatter } from 'react-chartjs-2';

Chart.register(LinearScale, PointElement, LineElement, Tooltip, Legend);


function StateScatter({census_data, state}) {
    const data = census_data.map(result => ({'x': result.income, 'y': result.case_ratio}) )
    const labels = census_data.map(result => (result.county_name + '\n Inc.: $' + result.income
                                                + '\n Pop.: ' + result.population) )

    const data_points = {
        labels,
        datasets: [ {
            label: 'county data',
            data,
            pointRadius: 5,
            pointBackgroundColor: 'rgba(200, 0, 100, 0.2)',
            pointBorderWidth: 2,
            pointBorderColor: 'rgba(200, 0, 100, 0.8)',
        } ]

    }

    const options = {
        scales: {
            y: { beginAtZero: true, title: {display: true, text: 'Case Count by Population'} },
            x: { beginAtZero: true, title: {display: true, text: 'Average Yearly House Hold Income'} },
        },
        plugins: { legend: {display: false, labels: {usePointStyle: true}} }
    }


    return (
        <>

            <div style = {{ marginLeft: "5vh", marginRight: "5vh", width: "400px"}}>

            <h5 style = {{ textAlign: "center" }}>Case Ratio by Average Income for Counties in {state}</h5>

            <p style = {{ textAlign: "center", fontSize: "12px" }}>
            This chart displays the normalized ratio of criminal cases from each county to that county&#39;s population
            by the average house hold income for that county. Hover over each point to see each county. </p>

            <Scatter
                options={options}
                data={data_points} />

            </div>
        </>

    )


}

export default StateScatter;