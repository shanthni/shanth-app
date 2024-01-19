import Form from 'react-bootstrap/Form';
import States from '../data/StateOptions.json'

function StateDDL({state, setState, setCounty}) {


    return (

    <Form.Select
        variant="dark"
        style={{
                    maxWidth: "300px",
                }}
        onChange = {e => {setState(e.target.value)
                          setCounty(0)} }
    >
      {

        States.States.map((result) => (<option key={result.id} value={result.id}> {result.state}
                                        </option>))

      }
    </Form.Select>
    );
}

export default StateDDL;