import DataTable from "react-data-table-component";
import { tableCustomStyles } from "../../styles";

function CaseTable({ county_data }) {
  const columns = [
    {
      name: "Offense",
      selector: (row) => row.offense,
      sortable: true,
      wrap: true,
    },
    {
      name: "Proceeding Date",
      selector: (row) => row.proceeding_date.slice(0, 16),
    },
    {
      name: "Disposition",
      selector: (row) => row.disposition,
      sortable: true,
      wrap: true,
    },
    {
      name: "Prison Time (months)",
      selector: (row) => row.prison_time,
      sortable: true,
    },
    {
      name: "Total Fine ($)",
      selector: (row) => row.fine,
      sortable: true,
    },
    {
      name: "Probation Time (months)",
      selector: (row) => row.prob_time,
      sortable: true,
    },
  ];

  return (
    <div>
      <h5 style={{ textAlign: "center", marginBottom: "10px" }}>
        {county_data.name} Terminated Cases
      </h5>

      <p style={{ textAlign: "center", marginBottom: "30px" }}>
        This table shows offenses from this county that have a recorded final
        disposition
      </p>

      <DataTable
        customStyles={tableCustomStyles}
        columns={columns}
        data={county_data.data}
        pagination
      />
    </div>
  );
}

export default CaseTable;