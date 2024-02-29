export default function onEachFeatureClosure(setCounty) {
  function changeCounty(e) {
    setCounty(e.target.feature.properties.county_id);
  }

  return function onEachFeature(feature, layer) {
    layer.bindPopup(feature.properties.NAME);

    layer.on({
      mouseover: layer.openPopup(),
      click: changeCounty,
    });
  };
}
