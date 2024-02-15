import DataTable from 'react-data-table-component';

function StateStats({stats}) {

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
            name: "Total Cases",
            selector: row => Math.round(row.case_count),
        },
        {
            name: "Average Prison Time",
            selector: row => Math.round(row.prison) + ' months',
        },
        {
            name: "Average Fine Amount",
            selector: row => '$' + row.fine.toFixed(2),
        },
        {
            name: "Average Probation Time",
            selector: row => Math.round(row.probation) + ' months',
        }
    ]


    return (

        <DataTable
            customStyles ={tableCustomStyles}
            columns={columns}
            data={stats}
        />

    );

}

export default StateStats;