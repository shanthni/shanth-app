import DataTable from 'react-data-table-component';

function CaseTable({county_data, state}) {

    if (county_data) {

        const tableCustomStyles = {
            headCells: {
                style: {
                    paddingLeft: '8px',
                    paddingRight: '8px',
                    fontSize: '15px',
                },
            },
            cells: {
                style: {
                    paddingLeft: '8px',
                    paddingRight: '8px',
                    fontSize: '15px'
                },
            },

        }

        const columns = [
            
            {
                name: "Offense",
                selector: row => row.offense,
                sortable: true,
                wrap: true
            },
            {
                name: "Proceeding Date",
                selector: row => row.proceeding_date.slice(0,16)
            },
            {
                name: "Disposition",
                selector: row => row.disposition,
                sortable: true,
                wrap: true
            },
            {
                name: "Prison Time (months)",
                selector: row => row.prison_time,
                sortable: true
            },
            {
                name: "Total Fine ($)",
                selector: row => row.fine,
                sortable: true
            },
            {
                name: "Probation Time (months)",
                selector: row => row.prob_time,
                sortable: true
            }
        ]


        return (
            <div style = {{width: '80%'}}>
                 <h5 style={{ textAlign: "center", marginBottom: "30px" }}>
                    {county_data.name} Terminated Cases</h5>

                <DataTable
                    customStyles ={tableCustomStyles}
                    columns={columns}
                    data={county_data.data}
                    pagination
                />

            </div>
        );
    }

    else if (state > 0) {
        return (
            <p> Select a County </p>

        )

    }


}

export default CaseTable;