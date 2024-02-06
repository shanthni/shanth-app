import { MapContainer, GeoJSON, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";


function CaseMap({state_geo, setCounty, state}) {


    function changeCounty(e) {
        setCounty(e.target.feature.properties.county_id)
    }


    function onEachFeature(feature, layer, avgCaseCount) {

        if (feature.properties) {
            layer.bindPopup(feature.properties.NAME);
            layer.options.fillOpacity = feature.properties.color;

            layer.on({
                mouseover: layer.openPopup(),
                mouseout: layer.closePopup(),
                click: changeCounty
            });

        }

    }

    return (

        <div>
            <h3 style={{ textAlign: "center", marginBottom: "30px" }}>
                {state} County Map</h3>

            <p style={{ textAlign: "center", marginBottom: "30px",  width: "600px" }}>
                This map displays the counties in {state}.
                The county&#39;s are shaded relative to the density of criminal cases to population in that county
                compared to other counties in the state.
                Darker color represents a higher density of cases.
                Click on each county to view the terminated criminal cases in that county. </p>


            <MapContainer
                key={state}
                style={{ height: "400px", width: "600px" }}
                zoom={7}
                center={state_geo.coordinates}>

                <TileLayer
                    opacity = '0.4'
                    attribution = '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                    url = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
                />

                <GeoJSON
                    data={state_geo.features}
                    onEachFeature = {onEachFeature}

                />
            </MapContainer>

        </div>

    );

}

export default CaseMap;