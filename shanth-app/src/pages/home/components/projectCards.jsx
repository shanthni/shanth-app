import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

function ProjectCards() {
  return (
    <>
      <Card style={{ width: "350px" }}>
        <Card.Body>
          <Card.Title>Criminal Court Cases Data</Card.Title>

          <Card.Text>
            This project creates data visualizations on federal criminal court
            cases from 2018 to 2023, with data from the federal judicial center
            IDB criminal data set.
          </Card.Text>

          <Button href="/projects/criminal-cases" variant="dark">
            Explore project
          </Button>
        </Card.Body>
      </Card>
    </>
  );
}

export default ProjectCards;
