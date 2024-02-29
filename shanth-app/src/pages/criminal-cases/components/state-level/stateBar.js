import {
  Chart,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";
import styles from "../../../styles.module.css";

Chart.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function StateBar({ offenseData, state }) {
  const data = offenseData.map((result) => result.off_count);
  const labels = offenseData.map((result) => result.offense);

  const dataPoints = {
    labels,
    datasets: [
      {
        data,
        backgroundColor: "rgba(249, 180, 45, 0.8)",
      },
    ],
  };

  const options = {
    scales: {
      y: {
        beginAtZero: true,
        title: { display: true, text: "Number of Cases Filed" },
      },
      x: {
        ticks: { callback: () => "" },
        title: { display: true, text: "Type of Offense" },
      },
    },
    plugins: { legend: { display: false } },
  };

  return (
    <>
      <div className = {styles.gridElement}>
        <h5 className = {styles.centerText}>
          Number of Filed Offenses for Top 10 Offenses in {state}
        </h5>

        <p className = {styles.centerText} style={{ fontSize: "12px" }}>
          This chart displays the top 10 filed offenses in criminal court cases
          in {state}. Hover over each bar to see the offense name and number of
          cases filed under that offense.{" "}
        </p>

        <Bar options={options} data={dataPoints} />
      </div>
    </>
  );
}

export default StateBar;
