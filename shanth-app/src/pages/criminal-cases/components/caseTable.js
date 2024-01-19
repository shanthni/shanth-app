import Table from 'react-bootstrap/Table';

function CaseTable({county_data}) {

    if (county_data) {


        return (

            <div>
                <Table responsive="sm">
                <thead>
                  <tr>

                    <th>Defendant Key</th>
                    <th>Offense</th>
                    <th>Proceeding Date</th>
                    <th>Disposition</th>
                    <th>Total Prison Time</th>
                    <th>Total Fine</th>
                    <th>Total Probation Time</th>

                  </tr>
                </thead>
                <tbody>
                  {county_data.map((data) =>
                      <tr key = {data.id}>

                        <td>{data.defendant_key}</td>
                        <td>{data.offense}</td>
                        <td>{data.proceeding_date}</td>
                        <td>{data.disposition}</td>
                        <td>{data.prison_time}</td>
                        <td>{data.fine}</td>
                        <td>{data.prob_time}</td>

                      </tr>
                     )}

                </tbody>
              </Table>


            </div>

        );
    }

    return (
        <div>
            <p> Loading... </p>
        </div>

    )
}

export default CaseTable;