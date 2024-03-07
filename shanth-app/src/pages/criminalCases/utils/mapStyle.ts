function getColor(d: number) {
  return d > 0.64
    ? "#bd0026"
    : d > 0.36
      ? "#f03b20"
      : d > 0.16
        ? "#fd8d3c"
        : d > 0.04
          ? "#fecc5c"
          : "#ffffb2";
}

export default function style(feature: { properties: { color: number } }) {
  return {
    fillColor: getColor(feature.properties.color),
    weight: 1,
    opacity: 1,
    color: "white",
    fillOpacity: 0.5,
  };
}
