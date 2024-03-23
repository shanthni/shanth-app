import CapitalizeState from "../utils/capitalizeState";

describe("State names are capitalized correctly", () => {
  test("Empty string", () => {
    expect(CapitalizeState("")).toBe("");
  });

  test("New Mexixo, all caps", () => {
    expect(CapitalizeState("NEW MEXICO")).toBe("New Mexico");
  });

  test("New Mexico, mixed case", () => {
    expect(CapitalizeState("nEw MeXICo")).toBe("New Mexico");
  });

  test("New Mexico, all lower", () => {
    expect(CapitalizeState("new mexico")).toBe("New Mexico");
  });

  test("Hawaii, all caps", () => {
    expect(CapitalizeState("HAWAII")).toBe("Hawaii");
  });

  test("Hawaii, mixed case", () => {
    expect(CapitalizeState("hAwaII")).toBe("Hawaii");
  });

  test("Hawaii, all lower", () => {
    expect(CapitalizeState("hawaii")).toBe("Hawaii");
  });
});
