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