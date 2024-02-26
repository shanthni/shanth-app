import React from "react";
import { useState } from "react";

import StateDDL from "./components/stateDDL";
import StateVisuals from "./components/stateVisuals";
import CountyVisuals from "./components/countyVisuals";


function Cases() {

    const [county, setCounty] = useState(0);
    const [state, setState] = useState(1);

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
                    Over 1 million criminal cases are analyzed in this project along with census and GIS data on over
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
                    state = {state}
                    setCounty = {setCounty}/>
            </div>

            <div style={{display: "flex", justifyContent: "center", marginTop: "5vh"}} >
               <CountyVisuals
                    county = {county} />
            </div>



        </>
    )
}

export default Cases;