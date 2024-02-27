export default function CapitalizeState(name) {
  const stateSplit = name.toLowerCase().split(" ");
  for (var i = 0; i < stateSplit.length; i++) {
    stateSplit[i] =
      stateSplit[i].charAt(0).toUpperCase() + stateSplit[i].slice(1);
  }

  return stateSplit.join(" ");
}
