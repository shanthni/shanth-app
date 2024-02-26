import React from "react";
import { useState, useEffect } from "react";
import CaseMap from "./state-level/caseMap";
import StateScatter from "./state-level/stateScatter";
import StateBar from "./state-level/stateBar";
import StateStats from "./state-level/stateStats";


function StateVisuals({state, setCounty}) {

    const [state_data, setState_data] = useState(null);

    useEffect(() => {
        const call_state_data = async () => {
            fetch('https://criminal-cases-shanth-7fea69fdcbd2.herokuapp.com/state-data/'+state)
            .then(response => response.json())
            .then(json => setState_data(json))
            .catch(error => console.error(error));
        };
        call_state_data()
    }, [state])

    if (state_data) {


        function CapitalizeState(name) {
            var stateSplit = (name.toLowerCase()).split(' ')
            for (var i = 0; i < stateSplit.length; i++) {
                stateSplit[i] = stateSplit[i].charAt(0).toUpperCase() + stateSplit[i].slice(1);
            }

            return stateSplit.join(' ')
        }

        return (
            <div>
                <div style={{display: "flex", justifyContent: "center"}}>
                    <h2> Criminal Cases: {CapitalizeState(state_data.state)} </h2>
                </div>

                <div style={{display: "flex", justifyContent: "center", marginTop: "5vh"}} >
                    < StateStats
                        stats = {state_data.stats} />
                </div>

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

    else {
        return (
            <div>
                <p> Select a State </p>
            </div>
        )

    }


}

export default StateVisuals;