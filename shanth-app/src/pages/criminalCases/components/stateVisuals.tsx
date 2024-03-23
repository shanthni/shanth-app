import React from "react";
import { useState, useEffect } from "react";
import { data } from "./models/stateData";
import styles from "../../styles.module.css";
import CapitalizeState from "../utils/capitalizeState";
import CaseMap from "./stateLevel/caseMap";
import StateScatter from "./stateLevel/stateScatter";
import StateBar from "./stateLevel/stateBar";
import StateStats from "./stateLevel/stateStats";

function StateVisuals({ state, setCounty }: { state: number; setCounty: any }) {
  const [stateData, setStateData] = useState<data | null>(null);

  useEffect(() => {
    const callStateData = async () => {
      fetch(
        `https://criminal-cases-shanth-7fea69fdcbd2.herokuapp.com/state-data/${state}`,
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
          Criminal Cases: {CapitalizeState(stateData.state)}
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
          id={stateData.id}
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
