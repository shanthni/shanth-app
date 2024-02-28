import React from "react";
import { useState, useEffect } from "react";
import styles from "../../styles.module.css";
import CapitalizeState from "../utils/capitalizeState";
import CaseMap from "./state-level/caseMap";
import StateScatter from "./state-level/stateScatter";
import StateBar from "./state-level/stateBar";
import StateStats from "./state-level/stateStats";

function StateVisuals({ state, setCounty }) {
  const [state_data, setState_data] = useState(null);

  useEffect(() => {
    const call_state_data = async () => {
      fetch(
        "https://criminal-cases-shanth-7fea69fdcbd2.herokuapp.com/state-data/" +
          state,
      )
        .then((response) => response.json())
        .then((json) => setState_data(json))
        .catch((error) => console.error(error));
    };
    call_state_data();
  }, [state]);

  return state_data ? (
    <div>
      <div className={styles.centerDetail}>
        <h2 className={styles.centerText}>
          {" "}
          Criminal Cases: {CapitalizeState(state_data.state)}{" "}
        </h2>
      </div>

      <div className={styles.center}>
        <StateStats stats={state_data.stats} />
      </div>

      <div className={styles.gridVisuals}>
        <StateScatter
          census_data={state_data.census_data}
          state={CapitalizeState(state_data.state)}
        />

        <StateBar
          offense_data={state_data.offense_data}
          state={CapitalizeState(state_data.state)}
        />
      </div>

      <div className={styles.center}>
        <CaseMap
          state_geo={state_data.geo_data}
          setCounty={setCounty}
          state={CapitalizeState(state_data.state)}
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
