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
import { barStyle } from "../../styles";
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

  return (
    <>
      <div className={styles.gridElement}>
        <h5 className={styles.centerText}>
          Number of Filed Offenses for Top 10 Offenses in {state}
        </h5>

        <p className={styles.centerText} style={{ fontSize: "12px" }}>
          This chart displays the top 10 filed offenses in criminal court cases
          in {state}. Hover over each bar to see the offense name and number of
          cases filed under that offense.{" "}
        </p>

        <Bar options={barStyle} data={dataPoints} />
      </div>
    </>
  );
}

export default StateBar;
