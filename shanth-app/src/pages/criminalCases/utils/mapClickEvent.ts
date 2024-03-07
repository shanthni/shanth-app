import { Feature } from "geojson";
import { Layer } from "leaflet";

export default function onEachFeatureClosure(setCounty: any) {
  function changeCounty(e: {
    target: { feature: { properties: { county_id: number } } };
  }) {
    setCounty(e.target.feature.properties.county_id);
  }

  return function onEachFeature(feature: Feature, layer: Layer) {
    layer.bindPopup(feature.properties.NAME);

    layer.on({
      click: changeCounty,
    });
  };
}
