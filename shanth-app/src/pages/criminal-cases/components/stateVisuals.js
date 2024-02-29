import React from "react";
import { useState, useEffect } from "react";
import styles from "../../styles.module.css";
import CapitalizeState from "../utils/capitalizeState";
import CaseMap from "./state-level/caseMap";
import StateScatter from "./state-level/stateScatter";
import StateBar from "./state-level/stateBar";
import StateStats from "./state-level/stateStats";

function StateVisuals({ state, setCounty }) {
  const [stateData, setStateData] = useState(null);

  useEffect(() => {
    const callStateData = async () => {
      fetch(
        "https://criminal-cases-shanth-7fea69fdcbd2.herokuapp.com/state-data/" +
          state,
      )
        .then((response) => response.json())
        .then((json) => setStateData(json))
        .catch((error) => console.error(error));
    };
    callStateData();
  }, [state]);

  return stateData ? (
    <div>
      <div className={styles.centerDetail}>
        <h2 className={styles.centerText}>
          {" "}
          Criminal Cases: {CapitalizeState(stateData.state)}{" "}
        </h2>
      </div>

      <div className={styles.center}>
        <StateStats stats={stateData.stats} />
      </div>

      <div className={styles.gridVisuals}>
        <StateScatter
          censusData={stateData.census_data}
          state={CapitalizeState(stateData.state)}
        />

        <StateBar
          offenseData={stateData.offense_data}
          state={CapitalizeState(stateData.state)}
        />
      </div>

      <div className={styles.center}>
        <CaseMap
          stateGeo={stateData.geo_data}
          setCounty={setCounty}
          state={CapitalizeState(stateData.state)}
        />
      </div>
    </div>
  ) : (
    <div>
      <p> Select a State </p>
    </div>
  );
}

export default StateVisuals;
