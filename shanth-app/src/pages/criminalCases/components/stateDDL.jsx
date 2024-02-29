import Form from "react-bootstrap/Form";
import States from "../data/stateOptions.json";
import styles from "../../styles.module.css";

function StateDDL({ setState, setCounty }) {
  return (
    <Form.Select
      className={styles.form}
      onChange={(e) => {
        setState(e.target.value);
        setCounty(0);
      }}
    >
      {States.States.map((result) => (
        <option key={result.id} value={result.id}>
          {" "}
          {result.state}
        </option>
      ))}
    </Form.Select>
  );
}

export default StateDDL;
