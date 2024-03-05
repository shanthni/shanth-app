export const tableCustomStyles = {
  headCells: {
    style: {
      paddingLeft: "8px",
      paddingRight: "8px",
      fontSize: "15px",
    },
  },
  cells: {
    style: {
      paddingLeft: "8px",
      paddingRight: "8px",
      fontSize: "15px",
    },
  },
};

export const scatterStyle = {
    scales: {
      y: {
        beginAtZero: true,
        title: { display: true, text: "Case Count by Population" },
      },
      x: {
        beginAtZero: true,
        title: { display: true, text: "Average Yearly House Hold Income" },
      },
    },
    plugins: { legend: { display: false, labels: { usePointStyle: true } } },
};

export const barStyle = {
  scales: {
    y: {
      beginAtZero: true,
      title: { display: true, text: "Number of Cases Filed" },
    },
    x: {
      ticks: { callback: () => "" },
      title: { display: true, text: "Type of Offense" },
    },
  },
  plugins: { legend: { display: false } },
};

