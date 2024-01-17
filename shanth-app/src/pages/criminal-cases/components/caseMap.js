import { MapContainer, GeoJSON } from "react-leaflet";
import "leaflet/dist/leaflet.css";


function CaseMap({county}) {

    if (county) {
    return (

        <div>
            <h3 style={{ textAlign: "center" }}>{county.name.meaning}</h3>

            <MapContainer
                key={county.name.meaning}
                style={{ height: "400px", width: "600px" }}
                zoom={7}
                center={county.coordinates}>
              <GeoJSON

                data={county.features}
              />
            </MapContainer>


        </div>

    );
    }

    return (
        <div>
            <p> Loading... </p>
        </div>

    )
}

export default CaseMap;