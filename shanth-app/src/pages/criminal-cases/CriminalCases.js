import React from "react";
import { useState, useEffect } from "react";
import StateDDL from "./components/stateDDL";
import StateVisuals from "./components/stateVisuals";
import CaseTable from "./components/caseTable";


function Cases() {

    const [state_data, setState_data] = useState(null);

    const [county_data, setCounty_data] = useState(null);

    const [county, setCounty] = useState(0);
    const [state, setState] = useState(1);


    useEffect(() => {
        const call_state_data = async () => {
            setCounty_data(null);
            fetch('https://criminal-cases-shanth-7fea69fdcbd2.herokuapp.com/state-data/'+state)
            .then(response => response.json())
            .then(json => setState_data(json))
            .catch(error => console.error(error));
        };
        call_state_data()
    }, [state])



    useEffect(() => {
        const call_county_data = async () => {
            fetch('https://criminal-cases-shanth-7fea69fdcbd2.herokuapp.com/county-data/'+county)
            .then(response => response.json())
            .then(json => setCounty_data(json))
            .catch(error => console.error(error));
        };
        call_county_data()
    }, [county])



    return (
        <>
            <div style={{display: "flex", justifyContent: "center", marginTop: "5vh"}} >
                <h1>
                    Federal Criminal Court Case Data Visualization
                </h1>

            </div>

            <div style={{display: "flex", justifyContent: "center", marginTop: "2vh"}} >
                <p style={{ textAlign: "center",  width: "80%" }}>
                    This project uses federal criminal court data from 2018 to 2023 to create interactive
                    visualizations and statistics on the state and county level.
                    Over 500,000 criminal cases are analyzed in this project along with census and GIS data on over
                    3,000 US counties.
                </p>
            </div>

           <div style={{display: "flex", justifyContent: "center", marginTop: "5vh"}} >
                <StateDDL
                    state = {state}
                    setState = {setState}
                    setCounty = {setCounty}/>
            </div>

            <div style={{display: "flex", justifyContent: "center", marginTop: "5vh"}} >
                < StateVisuals
                    state_data = {state_data}
                    setCounty = {setCounty}/>
            </div>

            <div style={{display: "flex", justifyContent: "center", marginTop: "5vh"}} >
               <CaseTable
                    county_data = {county_data}
                    state = {state}/>
            </div>



        </>
    )
}

export default Cases;