import axios from "axios";

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
    })
}