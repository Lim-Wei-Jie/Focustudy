import axios from "axios";

export function addTask(task_description) {
    let api_endpoint = `http://0.0.0.0:5000/create_task`;
    axios
        .post(api_endpoint, task_description)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
};

export function getTasks(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://0.0.0.0:5000/task_list`;
        axios
            .post(api_endpoint, email)
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

export function deleteTask(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://0.0.0.0:5000/task_list/delete`;
        axios
            .delete(api_endpoint, email, task_description)
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