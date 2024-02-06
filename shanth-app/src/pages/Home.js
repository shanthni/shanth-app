import React from "react";
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

const Home = () => {
    return (
        <>
            <div style={{ display: "flex", justifyContent: "center", marginTop: "5vh" }} >
                <h1>
                    Projects
                </h1>
            </div>

             <div style={{ display: "flex", justifyContent: "center", marginTop: "5vh" }} >
                <Card style={{ width: '50vh' }}>
                    <Card.Body>
                        <Card.Title>
                            Criminal Court Cases Data
                        </Card.Title>

                        <Card.Text>
                            This project creates data visualizations on federal criminal court
                            cases from 2018 to 2023, with data from the federal judicial center IDB criminal
                            data set.
                        </Card.Text>

                        <Button href="/projects/criminal-cases" variant="dark">Explore project</Button>

                    </Card.Body>
                </Card>

            </div>


             <div style={{ display: "flex", justifyContent: "center", marginTop: "5vh" }} >
                <h1>
                    About
                </h1>
            </div>

             <div style={{ display: "flex", justifyContent: "center", marginTop: "5vh" }} >
                <p style={{textAlign: "center"}}>
                    Hi, I'm Shanthni! I created this website to showcase some data analytics projects
                    that I'm working on. <br></br>
                    Check out the source code on my <a href="https://github.com/shanthni/shanth-app">github</a>.
                </p>
            </div>

        </>
    );
};

export default Home;