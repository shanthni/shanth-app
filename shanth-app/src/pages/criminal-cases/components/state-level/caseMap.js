import { MapContainer, GeoJSON, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";

import style from "../../utils/mapStyle";
import onEachFeatureClosure from "../../utils/mapClickEvent";

function CaseMap({ state_geo, setCounty, state }) {
  return (
    <div>
      <h3 style={{ textAlign: "center", marginBottom: "30px" }}>
        {state} County Map
      </h3>

      <p style={{ textAlign: "center", marginBottom: "30px", width: "600px" }}>
        This map displays the counties in {state}. The county&#39;s are shaded
        relative to the density of criminal cases to population in that county
        compared to other counties in the state. Darker color represents a
        higher density of cases. Click on each county to view the terminated
        criminal cases in that county.{" "}
      </p>

      <MapContainer
        key={state}
        style={{ height: "400px", width: "600px" }}
        zoom={7}
        center={state_geo.coordinates}
      >
        <TileLayer
          opacity="0.4"
          attribution='&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
          url="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <GeoJSON
          style={style}
          data={state_geo.features}
          onEachFeature={onEachFeatureClosure(setCounty)}
        />
      </MapContainer>
    </div>
  );
}

export default CaseMap;
