import axios from "axios";

export function getEvents() {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://0.0.0.0:5000/calendar`;
        axios
            .post(api_endpoint)
            .then((response) => {
                console.log(response.data);
                resolve(response.data)
            })
            .catch((error) => {
                console.log(error)
                reject([])
            });
    })