/*
 * Memento
 * Frontend 
 * API Client - Tests
*/


import API from "../src/API.js";
import assert from "assert";

describe("API", () => {
    describe("#constructor()", () => {
        it("should load configuration from environment", () => {
            const api = new API();
            assert(api.apiVersion === "0");
        });
    });
    describe("#create(type, params)", () => {
        it("should create organisation", async () => {
            const api = new API();
            const response = await api.create("org", {
                name: "James Bakery"
            });
            assert(response.id);
        });
    });
    describe("#query(type, params)", () => {
        it("should get orgs ids", async () => {
            const api = new API();
            const orgIds = await api.query("org", {"limit": 1, "skip": 0});
            assert(orgIds.length === 1);
        });
    });
    describe("#get(type, id)", () => {
        it("should get organisation", async () => {
            const api = new API();
            const orgIds = await api.query("org", {"limit": 1, "skip": 0});
            const org = await api.get("org", orgIds[0]);
            assert(org.name === "James Bakery");
        });
    });
    describe("#update(type, id, params)", () => {
        it("should update organisation", async () => {
            const api = new API();
            const orgIds = await api.query("org", {"limit": 1, "skip": 0});
            const response = await api.update("org", orgIds[0], {
                name: "John's Bakery"
            });
            assert(response.success);
        });
    });
    describe("#delete(type,id)", () => {
        it("should delete organisation", async() => {
            const api = new API();
            const orgIds = await api.query("org", {"limit": 1, "skip": 0});
            const response = await api.delete("org", orgIds[0]);
            assert(response.success);
        });
    });
});

