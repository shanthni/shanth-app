import React from "react";
import { useState } from "react";
import styles from "../styles.module.css";
import StateDDL from "./components/stateDDL";
import StateVisuals from "./components/stateVisuals";
import CountyVisuals from "./components/countyVisuals";

function Cases() {
  const [county, setCounty] = useState<number>(0);
  const [state, setState] = useState<number>(1);

  return (
    <>
      <div className={styles.center}>
        <h1>Federal Criminal Court Case Data Visualization</h1>
      </div>

      <div className={styles.centerDetail}>
        <p className={styles.centerText}>
          This project uses federal criminal court data from 2018 to 2023 to
          create interactive visualizations and statistics on the state and
          county level. <br></br> Over 1 million criminal cases are analyzed in
          this project along with census and GIS data on over 3,000 US counties.
        </p>
      </div>

      <div className={styles.center}>
        <StateDDL setState={setState} setCounty={setCounty} />
      </div>

      <div className={styles.center}>
        <StateVisuals state={state} setCounty={setCounty} />
      </div>

      <div className={styles.center}>
        <CountyVisuals county={county} />
      </div>
    </>
  );
}

export default Cases;
