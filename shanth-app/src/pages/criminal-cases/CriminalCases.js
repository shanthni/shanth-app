import React from "react";
import { useState, useEffect } from "react";
import StateDDL from "./components/stateDDL";
import StateVisuals from "./components/stateVisuals";
import CaseTable from "./components/caseTable";


function Cases() {

    const [state_data, setState_data] = useState(null);

    const [county_data, setCounty_data] = useState([]);

    const [county, setCounty] = useState(0);
    const [state, setState] = useState(1);


    useEffect(() => {
        const call_state_data = async () => {
            const response = await fetch('http://127.0.0.1:5000/state-data/'+state)
            setState_data(await response.json())
        };
        call_state_data()
    }, [state])



    useEffect(() => {
        const call_county_data = async () => {
            setCounty_data(null)
            const response = await fetch('http://127.0.0.1:5000/county-data/'+county)
            setCounty_data(await response.json())
        };
        call_county_data()
    }, [county])



    return (
        <>
            <div style={{display: "flex", justifyContent: "center", marginTop: "5vh"}} >
                <h1>
                    Criminal Court Cases Project
                </h1>
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
                    county_data = {county_data} />
            </div>



        </>
    )
}

export default Cases;