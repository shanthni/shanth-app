import { MapContainer, GeoJSON } from "react-leaflet";
import "leaflet/dist/leaflet.css";


function CaseMap({county_geo, setCounty}) {

    if (county_geo) {

        function changeCounty(e) {
            setCounty(e.target.feature.properties.county_id)
        }

        function onEachFeature(feature, layer) {
            if (feature.properties) {
                layer.bindPopup(feature.properties.NAME);
            }
            layer.on({
                click: changeCounty
            });
        }

        return (

            <div>
                <h3 style={{ textAlign: "center", marginBottom: "30px" }}>
                    {county_geo.name.meaning.charAt(0) + county_geo.name.meaning.slice(1).toLowerCase()} County Map</h3>

                <MapContainer
                    key={county_geo.name.meaning}
                    style={{ height: "400px", width: "600px" }}
                    zoom={7}
                    center={county_geo.coordinates}>

                  <GeoJSON
                    data={county_geo.features}
                    onEachFeature = {onEachFeature}

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