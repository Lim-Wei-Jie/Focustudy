import axios from "axios";

export function addTime(record) {
    let api_endpoint = `http://127.0.0.1:5000/addTime`;
    axios
        .post(api_endpoint, record)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
};

export function getTimesAll() {
    let api_endpoint = `http://127.0.0.1:5000/getTimesAll`;
    axios
        .get(api_endpoint)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
}

export function getTimesYear() {
    let api_endpoint = `http://127.0.0.1:5000/getTimesYear`;
    axios
        .get(api_endpoint)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
}

export function getTimesMonth() {
    let api_endpoint = `http://127.0.0.1:5000/getTimesMonth`;
    axios
        .get(api_endpoint)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
}

export function getTimesWeek() {
    let api_endpoint = `http://127.0.0.1:5000/getTimesWeek`;
    axios
        .get(api_endpoint)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
}