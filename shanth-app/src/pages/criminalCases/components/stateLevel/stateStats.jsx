import React from "react";
import DataTable from "react-data-table-component";
import { tableCustomStyles } from "../../styles";

function StateStats({ stats }) {
  const columns = [
    {
      name: "Total Cases",
      selector: (row) => Math.round(row.case_count),
    },
    {
      name: "Average Prison Time",
      selector: (row) => Math.round(row.prison) + " months",
    },
    {
      name: "Average Fine Amount",
      selector: (row) => "$" + row.fine.toFixed(2),
    },
    {
      name: "Average Probation Time",
      selector: (row) => Math.round(row.probation) + " months",
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
