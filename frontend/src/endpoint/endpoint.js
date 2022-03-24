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
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesAll`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                resolve(response.data.data.times)
            })
            .catch((error) => {
                console.log(error)
                reject(0)
            });
    })
}

export function getTimesYear(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesYear`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                resolve(response.data.data.times)
            })
            .catch((error) => {
                console.log(error)
                reject(0)
            });
    })
}

export function getTimesMonth(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesMonth`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                resolve(response.data.data.times)
            })
            .catch((error) => {
                console.log(error)
                reject(0)
            });
    })
}

export function getTimesDay(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesDay`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                resolve(response.data.data.times)
            })
            .catch((error) => {
                console.log(error)
                reject(0)
            });
    })
}