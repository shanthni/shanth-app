import React from "react";
import { useState, useEffect } from "react";
import CaseTable from "./countyLevel/caseTable";

function CountyVisuals({ county }: { county: number }) {
  const [countyData, setCountyData] = useState(null);

  useEffect(() => {
    const callCountyData = async () => {
      fetch(
        "https://criminal-cases-shanth-7fea69fdcbd2.herokuapp.com/county-data/" +
          county,
      )
        .then((response) => response.json())
        .then((json) => setCountyData(json))
        .catch((error) => console.error(error));
    };
    callCountyData();
  }, [county]);

  return countyData ? (
    <div style={{ width: "80%" }}>
      <CaseTable countyData={countyData} />
    </div>
  ) : (
    <div>
      <p> Select a County </p>
    </div>
  );
}

export default CountyVisuals;
