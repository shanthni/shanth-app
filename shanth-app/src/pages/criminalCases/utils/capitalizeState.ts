export default function CapitalizeState(name: string) {
  const stateSplit = name.toLowerCase().split(" ");
  for (let i = 0; i < stateSplit.length; i++) {
    stateSplit[i] =
      stateSplit[i].charAt(0).toUpperCase() + stateSplit[i].slice(1);
  }

  return stateSplit.join(" ");
}
