import axios from "axios";

export function catchRate(record) {
    let api_endpoint = `http://127.0.0.1:5000/posttime`;
    axios
        .post(api_endpoint, record)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
};
