import axios from "axios";

// Add time record
export function addTime(record) {
    let api_endpoint = `http://127.0.0.1:5000/addTime`;
    axios
        .post(api_endpoint, record)
        .then((response) => {
            // {"code": 201, "data": "New time recorded."}
            console.log(response.data);
        })
        .catch((error) => {
            // {"code": 500, "data": "An error occurred creating time record."}
            console.log(error)
        });
};

// Retrieve all times
export function getTimesAll(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesAll`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                // Array of {"range": year(int), "total": hours(float)}
                resolve(response.data.data.times)
            })
            .catch((error) => {
                console.log(error)
                // No data screen
                reject([])
            });
    })
}

// Retrieve times this year
export function getTimesYear(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesYear`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                // Array of {"range": month(str), "total": hours(float)}
                resolve(response.data.data.times)
            })
            .catch((error) => {
                console.log(error)
                // No data screen
                reject([])
            });
    })
}

// Retrieve times this month
export function getTimesMonth(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesMonth`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                // Array of {"range": day(int), "total": hours(float)}
                resolve(response.data.data.times)
            })
            .catch((error) => {
                console.log(error)
                // No data screen
                reject([])
            });
    })
}

// Retrieve times from last 7 days (today inclusive)
export function getTimesDay(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesDay`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                // Array of {"range": day(int), "total": hours(float)}
                resolve(response.data.data.times)
            })
            .catch((error) => {
                console.log(error)
                // No data screen
                reject([])
            });
    })
}