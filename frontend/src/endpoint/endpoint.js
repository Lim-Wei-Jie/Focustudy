import axios from "axios";

export function catchRate(record) {
    let api_endpoint = `http://127.0.0.1:5000/addRating`;
    axios
        .post(api_endpoint, record)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
};

export function getRate(record) {
    let api_endpoint = `http://127.0.0.1:5000/getRating`;
    axios
        .get(api_endpoint, record)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
};



