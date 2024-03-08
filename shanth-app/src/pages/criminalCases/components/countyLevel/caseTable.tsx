import React from "react";
import DataTable from "react-data-table-component";
import styles from "../../../styles.module.css";
import { tableCustomStyles } from "../../styles";
import { data, cases } from "../models/countyData";

function CaseTable({ countyData }: {countyData: data}) {
  const columns = [
    {
      name: "Offense",
      selector: (row: cases) => row.offense,
      sortable: true,
      wrap: true,
    },
    {
      name: "Proceeding Date",
      selector: (row: cases) => row.proceeding_date.slice(0, 16),
    },
    {
      name: "Disposition",
      selector: (row: cases) => row.disposition,
      sortable: true,
      wrap: true,
    },
    {
      name: "Prison Time (months)",
      selector: (row: cases) => row.prison_time,
      sortable: true,
    },
    {
      name: "Total Fine ($)",
      selector: (row: cases) => row.fine,
      sortable: true,
    },
    {
      name: "Probation Time (months)",
      selector: (row: cases) => row.prob_time,
      sortable: true,
    },
  ];

  return (
    <div>
      <h5 className={styles.centerText}>{countyData.name} Terminated Cases</h5>

      <p className={styles.centerText} style={{ marginBottom: "30px" }}>
        This table shows offenses from this county that have a recorded final
        disposition
      </p>

      <DataTable
        customStyles={tableCustomStyles}
        columns={columns}
        data={countyData.data}
        pagination
      />
    </div>
  );
}

export default CaseTable;
