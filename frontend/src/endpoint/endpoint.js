import axios from "axios";

// ----------------------------------------------------------------------------------------------------------------

// TASK

export function addTask(email, task_description) {
    let api_endpoint = `http://127.0.0.1:5000/task_list/create`;
    axios
        .post(api_endpoint, email, task_description)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
};

export function getTasks(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/task_list`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                // console.log(response.data);
                resolve(response.data)
            })
            .catch((error) => {
                console.log(error)
                reject([])
            });
    })
}

export function deleteTask(email, task_id) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/task_list/delete`;
        axios
            .post(api_endpoint, email, task_id)
            .then((response) => {
                console.log(response.data);
                resolve(response.data)
            })
            .catch((error) => {
                console.log(error)
                reject([])
            });
    });
}

// ----------------------------------------------------------------------------------------------------------------

// TIME

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
}

// ----------------------------------------------------------------------------------------------------------------

// RATING

// Add rating record
export function addRating(record) {
    let api_endpoint = "http://127.0.0.1:5000/addRating";
    axios
        .post(api_endpoint, record)
        .then((response) => {
            // { "code": 201, "data": "Rating posted." }
            console.log(response.data);
        })
        .catch((error) => {
            // { "code": 500, "data": "An error occurred creating time record." }
            console.log(error)
        });
}

// ----------------------------------------------------------------------------------------------------------------

// RECORD SESSION

export function recordSession(sessionData) {
    return new Promise((resolve, reject) => {
        let api_endpoint = "http://127.0.0.1:5100/record_session"
        axios
            .post(api_endpoint, sessionData)
            .then((res) => {
                console.log(res.data);
                // returns to rating.vue
                resolve(res.data)
            })
            .catch((err) => {
                reject(err)
            })
    })
}

// ----------------------------------------------------------------------------------------------------------------

// SPOTIFY

export function getTopTracks() {
    return new Promise((resolve, reject) => {
        let api_endpoint = 'http://127.0.0.1:5005/music';
        axios
            .get(api_endpoint)
            .then((response) => {
                console.log(response.data.data);
                resolve(response.data.data);
            })
            .catch((error) => {
                console.log(error)
                reject([])
            });
    })
}