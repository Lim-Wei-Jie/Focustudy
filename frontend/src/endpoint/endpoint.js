import axios from "axios";

// Add time record
export function addTask(task_description) {
    let api_endpoint = `http://0.0.0.0:5000/create_task`;
    axios
        .post(api_endpoint, task_description)
        .then((response) => {
            // {"code": 201, "data": "New task recorded."}
            console.log(response.data);
        })
        .catch((error) => {
            // {"code": 500, "data": "An error occurred creating task."}
            console.log(error)
        });
};

// Retrieve all times
export function getTasks(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://0.0.0.0:5000/task_list`;
        axios
            .post(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                // Array of {"range": year(int), "total": hours(float)}
                resolve(response.data)
            })
            .catch((error) => {
                console.log(error)
                // No data screen
                reject([])
            });
    })
}

// Retrieve all times
export function deleteTask(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://0.0.0.0:5000/task_list/delete`;
        axios
            .delete(api_endpoint, email)
            .then((response) => {
                console.log(response.data);
                resolve(response.data)
            })
            .catch((error) => {
                console.log(error)
                reject([])
            });
    })
}