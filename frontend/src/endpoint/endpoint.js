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

export function getTimesAll(email) {
    let api_endpoint = `http://127.0.0.1:5000/getTimesAll`;
    axios
        .post(api_endpoint, email)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
}

export function getTimesYear(email) {
    let api_endpoint = `http://127.0.0.1:5000/getTimesYear`;
    axios
        .post(api_endpoint, email)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
}

export function getTimesMonth(email) {
    let api_endpoint = `http://127.0.0.1:5000/getTimesMonth`;
    axios
        .post(api_endpoint, email)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
}

export function getTimesWeek(email) {
    let api_endpoint = `http://127.0.0.1:5000/getTimesWeek`;
    axios
        .post(api_endpoint, email)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
}