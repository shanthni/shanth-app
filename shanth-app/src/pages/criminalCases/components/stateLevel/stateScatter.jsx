import React from "react";
import {
  Chart,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Scatter } from "react-chartjs-2";
import { scatterStyle } from "../../styles";
import styles from "../../../styles.module.css";

Chart.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

function StateScatter({ censusData, state }) {
  const data = censusData.map((result) => ({
    x: result.income,
    y: result.case_ratio,
  }));
  const labels = censusData.map(
    (result) =>
      result.county_name +
      "\n Inc.: $" +
      result.income +
      "\n Pop.: " +
      result.population,
  );

  const dataPoints = {
    labels,
    datasets: [
      {
        label: "county data",
        data,
        pointRadius: 5,
        pointBackgroundColor: "rgba(200, 0, 100, 0.2)",
        pointBorderWidth: 2,
        pointBorderColor: "rgba(200, 0, 100, 0.8)",
      },
    ],
  };

  return (
    <>
      <div className={styles.gridElement}>
        <h5 className={styles.centerText}>
          Case Ratio by Average Income for Counties in {state}
        </h5>

        <p className={styles.centerText} style={{ fontSize: "12px" }}>
          This chart displays the normalized ratio of criminal cases from each
          county to that county&#39;s population by the average house hold
          income for that county. Hover over each point to see each county.{" "}
        </p>

        <Scatter options={scatterStyle} data={dataPoints} />
      </div>
    </>
  );
}

export default StateScatter;
