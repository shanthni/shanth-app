import Form from 'react-bootstrap/Form';
import States from '../data/StateOptions.json'

function StateDDL({state, setState}) {


    return (

    <Form.Select
        variant="dark"
        style={{
                    maxWidth: "300px",
                }}
        onChange = {e => setState(e.target.value)}
    >
      {

        States.States.map((result) => (<option value={result.id}> {result.state}
                                        </option>))

      }
    </Form.Select>
    );
}

export default StateDDL;