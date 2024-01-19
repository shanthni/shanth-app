import React from "react";
import { useState, useEffect } from "react";
import StateDDL from "./components/stateDDL";
import CaseMap from "./components/caseMap";
import CaseTable from "./components/caseTable";


function Cases() {

    const [county_geo, setCounty_geo] = useState(null);
    const [county_data, setCounty_data] = useState([]);
    const [county, setCounty] = useState(0);
    const [state, setState] = useState(1);

    useEffect(() => {
        const counties_geo = async () => {
            const response = await fetch('http://127.0.0.1:5000/county-data/'+state)
            setCounty_geo(await response.json())
        };
        counties_geo()
    }, [state])

    useEffect(() => {
        const counties_cases = async () => {
            setCounty_data(null)
            const response = await fetch('http://127.0.0.1:5000/county-cases/'+county)
            setCounty_data(await response.json())
        };
        counties_cases()
    }, [county])


    return (
        <div>
            <div
                style={{
                    display: "flex",
                    justifyContent: "center",
                    marginTop: "5vh"
                }}
            >
                <h1>
                    Criminal Court Cases Project
                </h1>
            </div>

            <div
                style={{
                    display: "flex",
                    justifyContent: "center",
                    marginTop: "5vh"
                }}
            >
                <StateDDL
                    state = {state}
                    setState = {setState}
                    setCounty = {setCounty}/>
            </div>

            <div
                style={{
                    display: "flex",
                    justifyContent: "center",
                    marginTop: "5vh"
                }}
            >
                < CaseMap
                    county_geo = {county_geo}
                    setCounty = {setCounty}/>
            </div>

            <div
                style={{
                    display: "flex",
                    justifyContent: "center",
                    marginTop: "5vh"
                }}
            >
               <CaseTable
                    county_data = {county_data} />
            </div>



        </div>
    )
}

export default Cases;