import { MapContainer, GeoJSON, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";


function CaseMap({state_geo, setCounty, state}) {


    function changeCounty(e) {
        setCounty(e.target.feature.properties.county_id)
    }


    function onEachFeature(feature, layer) {
        layer.bindPopup(feature.properties.NAME);

        layer.on({
            mouseover: layer.openPopup(),
            click: changeCounty
        });
    }

    function getColor(d) {
        return d > 0.64 ? '#bd0026' :
               d > 0.36  ? '#f03b20' :
               d > 0.16  ? '#fd8d3c' :
               d > 0.04  ? '#fecc5c' :
                          '#ffffb2';
    }

    function style(feature) {
        return {
            fillColor: getColor(feature.properties.color),
            weight: 1,
            opacity: 1,
            color: 'white',
            fillOpacity: 0.5
        };
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
                    style={style}
                    data={state_geo.features}
                    onEachFeature = {onEachFeature}

                />
            </MapContainer>

        </div>

    );

}

export default CaseMap;