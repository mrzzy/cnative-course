/*
 * Memento
 * Frontend 
 * API Client
*/

import assert from "assert";
import fetch from "cross-fetch";
import dotenv from "dotenv";

// defines an api client to interface with the backend api
export default class API {
    // constructs client to interface with the api
    constructor() {
        // load config from environment 
        dotenv.config();
        this.apiHost = process.env.REACT_APP_API_HOST;
        this.apiVersion = process.env.REACT_APP_API_VERSION;
        this.protocol = process.env.REACT_APP_API_PROTOCOL;
        console.log(process.env.REACT_APP_API_VERSION);
        // check protocol support
        assert(this.protocol === "http" || this.protocol === "https");
    
        // build api root url from configuration
        this.apiRoot = `${this.protocol}://${this.apiHost}/api/v${this.apiVersion}`

        // build api object - service mapping 
        this.objectServiceMap = {
            // iam objects
            "org": "iam",
            "user": "iam",
            "team": "iam",
            "manage": "iam",
            // assignment service
            "task": "assignment",
            "event": "assignment",
            "assign": "assignment",
            // notification service
            "notify": "notification",
            "channel": "notification",
        };
    }

    // convert the given set of url param to url param string
    // returns the url param string 
    convertUrl(params) {
        return "?" + Object.entries(params)
            .map(([key, value]) => `${key}=${value}`).join("&");
    }

    // returns true if given type is supported, otherwise false
    supports(type)  {
        return type in this.objectServiceMap
    }

    // build object url 
    // type - type of object to build. Must be supported
    objectUrl(type) {
        // check object type supported
        assert(this.supports(type));
        // build object url
        const service = this.objectServiceMap[type];
        const objectUrl = `${this.apiRoot}/${service}/${type}`;
        return objectUrl;
    }
    
    // query objects
    // type - type of object to query
    // params - query parameters to pass on query
    async query(type, params={}) {
        // build query url
        const queryParams = this.convertUrl(params);
        const queryUrl = `${this.objectUrl(type)}s${queryParams}`;
        // perform query request
        const response = await fetch(queryUrl);
        return await response.json();
    }

    // get object
    // type - type of object to get
    // id - id of the object to get
    async get(type, id) {
        const objUrl = `${this.objectUrl(type)}/${id}`;
    
        // perform get request
        const response = await fetch(objUrl, {
            method: "GET",
            mode: "cors",
            cache: "no-cache"
        });

        return await response.json();
    }

    // create object
    // type - type of object to create
    // params - params to pass to create object
    // returns api response
    async create(type, params) {
        // perform create request 
        const response = await fetch(this.objectUrl(type), {
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(params)
        });
        
        return await response.json();
    }
    
    // update object
    // type - type of object to update
    // id - id of the object to update
    // params - params to pass to update object
    // returns api response
    async update(type, id, params) {
        const objUrl = `${this.objectUrl(type)}/${id}`;

        // perform update request 
        const response = await fetch(objUrl, {
            method: "PATCH",
            mode: "cors",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(params)
        });
        
        return await response.json();
    }

    // delete object
    // type - type of object to delete
    // id - id of the object to delete 
    // returns api response
    async delete(type, id) {
        // perform delete request
        const objUrl = `${this.objectUrl(type)}/${id}`;
        const response = await fetch(objUrl, {
            method: "DELETE",
            mode: "cors",
            cache: "no-cache"
        });
        
        return await response.json();
    }
}
