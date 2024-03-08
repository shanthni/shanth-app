import React from "react";
import { MapContainer, GeoJSON, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import styles from "../../../styles.module.css";
import style from "../../utils/mapStyle";
import onEachFeatureClosure from "../../utils/mapClickEvent";
import { geo } from "../models/stateData";

function CaseMap({
  stateGeo,
  setCounty,
  state,
  id,
}: {
  stateGeo: geo;
  setCounty: any;
  state: String;
  id: number;
}) {
  return (
    <div>
      <h3 className={styles.centerText}>{state} County Map</h3>

      <p
        className={styles.centerText}
        style={{ width: "600px", marginBottom: "30px" }}
      >
        This map displays the counties in {state}. The county&#39;s are shaded
        relative to the density of criminal cases to population in that county
        compared to other counties in the state. Darker color represents a
        higher density of cases. Click on each county to view the terminated
        criminal cases in that county.{" "}
      </p>

      <MapContainer
        key={id}
        style={{ height: "400px", width: "600px" }}
        zoom={7}
        center={stateGeo.coordinates}
      >
        <TileLayer
          opacity={0.4}
          attribution='&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
          url="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <GeoJSON
          style={style}
          data={stateGeo.features}
          onEachFeature={onEachFeatureClosure(setCounty)}
        />
      </MapContainer>
    </div>
  );
}

export default CaseMap;
