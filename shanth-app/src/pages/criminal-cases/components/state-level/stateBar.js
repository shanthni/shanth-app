import {
  Chart,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Scatter, Bar } from 'react-chartjs-2';

Chart.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);


function StateBar({offense_data, state}) {

    const data = offense_data.map(result => (result.off_count) )
    const labels = offense_data.map(result => (result.offense) )

    const data_points = {
        labels,
        datasets: [ {
            data,
            backgroundColor: 'rgba(249, 180, 45, 0.8)',
        } ]

    }

    const options = {
        scales: {
            y: { beginAtZero: true, title: {display: true, text: 'Number of Cases Filed'} },
            x: { ticks: { callback: () => ('') }, title: {display: true, text: 'Type of Offense'} },
        },
        plugins: { legend: {display: false} }
    }


    return (
        <>

            <div style = {{ marginLeft: "5vh", marginRight: "5vh", width: "400px"}}>

            <h5 style = {{ textAlign: "center" }}>Number of Filed Offenses for Top 10 Offenses in {state}</h5>

            <p style = {{ textAlign: "center", fontSize: "12px" }}>
            This chart displays the top 10 filed offenses in criminal court cases in {state}. Hover over each
             bar to see the offense name and number of cases filed under that offense. </p>


            <Bar
                options={options}
                data={data_points} />

            </div>
        </>

    )


}

export default StateBar;