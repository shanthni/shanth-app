import React from "react";
import styles from "../styles.module.css";
import ProjectCards from "./components/projectCards";

const Home = () => {
  return (
    <>
      <div className={styles.center}>
        <h1>Projects</h1>
      </div>

      <div className={styles.center} style={{ marginTop: "0vh" }}>
        <ProjectCards />
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
