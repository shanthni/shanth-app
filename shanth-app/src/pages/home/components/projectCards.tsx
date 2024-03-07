import React from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import styles from "../../styles.module.css";

function ProjectCards() {
  return (
    <div className={styles.gridVisuals}>
      <Card className={styles.card}>
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

      <Card className={styles.card}>
        <Card.Body>
          <Card.Title>US Mortality Rates Exploration</Card.Title>

          <Card.Text>
            Upcoming project exploring US mortality rates and its causes, using
            mortality data from CDC wonder.
          </Card.Text>

          <Button href="/projects/us-mortality" variant="dark">
            Explore project
          </Button>
        </Card.Body>
      </Card>
    </div>
  );
}

export default ProjectCards;
