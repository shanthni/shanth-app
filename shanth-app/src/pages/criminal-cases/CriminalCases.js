import React from "react";
import { useState, useEffect } from "react";
import StateDDL from "./components/stateDDL";
import CaseMap from "./components/caseMap";


function Cases() {
    const [county, setCounty] = useState(null);
    const [state, setState] = useState(1);

    useEffect(() => {
        const counties = async () => {
            const response = await fetch('http://127.0.0.1:5000/county-data/'+state)

            setCounty(await response.json())
        };
        counties()
    }, [state])



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
                    state={state}
                    setState={setState}
                />
            </div>

            <div
                style={{
                    display: "flex",
                    justifyContent: "center",
                    marginTop: "5vh"
                }}
            >
                < CaseMap
                    county = {county} />
            </div>

        </div>
    )
}

export default Cases;