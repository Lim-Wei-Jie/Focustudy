import axios from "axios";

export function addTime(duration) {
    let api_endpoint = `http://127.0.0.1:5000/addTime`;
    let timeRecord = {
        "startDate": new Date().toISOString().slice(0, 10),
        "duration": duration
    }
    axios
        .post(api_endpoint, timeRecord)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
};