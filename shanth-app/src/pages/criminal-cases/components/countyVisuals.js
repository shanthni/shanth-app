import React from "react";
import { useState, useEffect } from "react";
import CaseTable from "./county-level/caseTable";


function CountyVisuals({county}) {

    const [county_data, setCounty_data] = useState(null);

    useEffect(() => {
        const call_county_data = async () => {
            fetch('https://criminal-cases-shanth-7fea69fdcbd2.herokuapp.com/county-data/'+county)
            .then(response => response.json())
            .then(json => setCounty_data(json))
            .catch(error => console.error(error));
        };
        call_county_data()
    }, [county])


    if (county_data) {

        return (

            <div style={{ width: "80%"}} >
                < CaseTable
                    county_data = {county_data} />
            </div>

        )

    }

    else {
        return (
            <div>
                <p> Select a County </p>
            </div>
        )

    }


}

export default CountyVisuals;