import axios from "axios";

export default function getTopTracks() {
    return new Promise((resolve, reject) => {
        let api_endpoint = 'http://localhost:5000/music';
        axios
            .post(api_endpoint)
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