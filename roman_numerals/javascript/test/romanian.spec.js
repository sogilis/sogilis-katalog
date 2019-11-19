const { translateRomanian } = require("../src/romanian");
const { expect } = require("chai");

describe("translateRomanian", () => {
  it("should translate input I", () => {
    expect(translateRomanian("I")).to.equal(1);
  });

  it("should translate input II", () => {
    expect(translateRomanian("II")).to.equal(2);
  });

  it("should translate input III", () => {
    expect(translateRomanian("III")).to.equal(3);
  });

  it("should not translate empty string", () => {
    expect(translateRomanian("")).to.equal(undefined);
  });
});
