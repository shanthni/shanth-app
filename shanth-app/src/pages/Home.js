import React from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import styles from "./styles.module.css";

const Home = () => {
  return (
    <>
      <div className={styles.center}>
        <h1>Projects</h1>
      </div>

      <div className={styles.center}>
        <Card style={{ width: "25%" }}>
          <Card.Body>
            <Card.Title>Criminal Court Cases Data</Card.Title>

            <Card.Text>
              This project creates data visualizations on federal criminal court
              cases from 2018 to 2023, with data from the federal judicial
              center IDB criminal data set.
            </Card.Text>

            <Button href="/projects/criminal-cases" variant="dark">
              Explore project
            </Button>
          </Card.Body>
        </Card>
      </div>

      <div className={styles.center}>
        <h1>About</h1>
      </div>

      <div className={styles.centerDetail}>
        <p className={styles.centerText}>
          Hi, I'm Shanthni! I created this website to showcase some data
          analytics projects that I'm working on. <br></br>
          Check out the source code on my{" "}
          <a href="https://github.com/shanthni/shanth-app">github</a>.
        </p>
      </div>
    </>
  );
};

export default Home;
