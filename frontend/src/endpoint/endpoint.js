import axios from "axios";

// ----------------------------------------------------------------------------------------------------------------

// TIME: ADD RECORD

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

// ----------------------------------------------------------------------------------------------------------------

// TIME: GET RECORDS

// Retrieve all times
export function getTimesAll(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5100/getTimesAll`;
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
        let api_endpoint = `http://127.0.0.1:5100/getTimesYear`;
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
        let api_endpoint = `http://127.0.0.1:5100/getTimesMonth`;
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

// Retrieve times from last 7 days (today inclusive)
export function getTimesDay(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5100/getTimesDay`;
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

// ----------------------------------------------------------------------------------------------------------------

// RATING: ADD RECORD

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

// RATING: GET RECORDS

// Retrieve all ratings
export function getRatings(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5100/getRatings`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                resolve(response.data)
            })
            .catch((error) => {
                reject(error)
            });
    })
};

// ----------------------------------------------------------------------------------------------------------------

// Call record_session complex MS
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

// Call display_sessions complex MS
export function displaySessions(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = "http://127.0.0.1:5200/display_sessions"
        axios
            .post(api_endpoint, email)
            .then((res) => {
                console.log(res.data);
                // returns to 
                resolve(res.data)
            })
            .catch((err) => {
                reject(err)
            })
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