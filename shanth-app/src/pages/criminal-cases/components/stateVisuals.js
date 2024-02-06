import React from "react";
import CaseMap from "./state-level/caseMap";
import StateScatter from "./state-level/stateScatter";
import StateBar from "./state-level/stateBar";


function StateVisuals({state_data, setCounty}) {
    if (state_data) {

    function CapitalizeState(state) {
        var stateSplit = (state.toLowerCase()).split(' ')
        for (var i = 0; i < stateSplit.length; i++) {
            stateSplit[i] = stateSplit[i].charAt(0).toUpperCase() + stateSplit[i].slice(1);
        }

        return stateSplit.join(' ')
    }

    return (
        <div>
            <div style={{display: "grid", gridTemplateColumns: "1fr 1fr", justifyContent: "center", marginTop: "5vh"}} >
                < StateScatter
                    census_data = {state_data.census_data}
                    state = {CapitalizeState(state_data.state)}/>

                 < StateBar
                    offense_data = {state_data.offense_data}
                    state = {CapitalizeState(state_data.state)}/>
            </div>

            <div style={{display: "flex", justifyContent: "center", marginTop: "5vh"}} >
                < CaseMap
                    state_geo = {state_data.geo_data}
                    setCounty = {setCounty}
                    state = {CapitalizeState(state_data.state)}/>
            </div>

        </div>
    )

    }


}

export default StateVisuals;