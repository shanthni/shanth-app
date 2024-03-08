import React from "react";
import DataTable from "react-data-table-component";
import { tableCustomStyles } from "../../styles";
import { stats } from "../models/stateData";

function StateStats({ stats }: { stats: stats[] }) {
  const columns = [
    {
      name: "Total Cases",
      selector: (row: stats) => Math.round(row.case_count),
    },
    {
      name: "Average Prison Time",
      selector: (row: stats) => Math.round(row.prison) + " months",
    },
    {
      name: "Average Fine Amount",
      selector: (row: stats) => "$" + row.fine.toFixed(2),
    },
    {
      name: "Average Probation Time",
      selector: (row: stats) => Math.round(row.probation) + " months",
    },
  ];

  return (
    <DataTable
      customStyles={tableCustomStyles}
      columns={columns}
      data={stats}
    />
  );
}

export default StateStats;
