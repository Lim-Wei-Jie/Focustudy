import axios from "axios";

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
};

// Retrieve all times
export function getTimesAll(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesAll`;
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
        let api_endpoint = `http://127.0.0.1:5000/getTimesYear`;
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
        let api_endpoint = `http://127.0.0.1:5000/getTimesMonth`;
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

// Retrieve times from last 7 days (today inclusive)
export function getTimesDay(email) {
    return new Promise((resolve, reject) => {
        let api_endpoint = `http://127.0.0.1:5000/getTimesDay`;
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


export function catchRate(record) {
    let api_endpoint = "http://localhost:5100/addRating";
    axios
        .post(api_endpoint, record)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.log(error)
        });
}


export function getAllRatings () {
    const response =
        fetch("http://127.0.0.1:5008/getRating")
            .then(response => response.json())
            .then(data => {
                console.log(response);
                if (data.code === 404) {
                    // no book in db
                    console.log('fail');
                } else {

                    console.log(data)
                    return data
                    
                }
            })
            .catch(error => {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                console.log(this.message + error);

            });
}


export function testRate() {
    let method = 'get' // ex. get | post | put | delete , etc
    let url = "http://127.0.0.1:5000/getRating"
    let userdata = 447
    let morningGPAList = []
    let afternoonGPAList = []
    let nightGPAList = []

    return axios[method](url)
        .then((response) => {
            // success
            //-> save response to state, notification
            //console.log(response.data.data.ratings)
           
            //console.log(response.data.data.ratings)
            //console.log(this.userdata)
            userdata = response.data.data.ratings
            

            return userdata // pass to finish
        })
        .catch((error) => {
            // failed
            //-> prepare, notify, handle error
            //let error = 2
            console.log(error)

            return false // pass to finish
        }).then((resultBoolean) => {
            // do something after success or error

                for (const [key1, value1] of Object.entries(userdata)) {

                    console.log({key1})

                    for (const [key, value] of Object.entries(value1))
                    {
                        //console.log(`${key}`);
                        if (`${key}` == "morningGPA" )
                        {
                            //console.log('here')
                            //console.log('hahaha')
                            if (Number(`${value}`) != 0)
                            {
                                morningGPAList.push(Number(`${value}`))
                            }
                            
                        }

                        if (`${key}` == "afternoonGPA" )
                        {
                            //console.log('here')
                            //console.log('hahaha')
                            if (Number(`${value}`) != 0)
                            {
                                afternoonGPAList.push(Number(`${value}`))
                            }
                            
                            //console.log(`${value}`)
                        }

                        if (`${key}` == "nightGPA" )
                        {
                            //console.log('here')
                            //console.log('hahaha')
                            if (Number(`${value}`) != 0)
                            {
                                nightGPAList.push(Number(`${value}`))
                            }
                            
                            //console.log(`${value}`)
                        }
                    }
                    
                }

    
        console.log(morningGPAList)
        return resultBoolean // for await purpose
    })

            

};


export function getAllRatings () {
    return new Promise((resolve, reject) => {
        let api_endpoint = "http://localhost:5100/getRating"
        axios
            .get(api_endpoint)
            .then((res) => {
                // definitely need to cut this shit LOL
                console.log(res.data.data.rating_result.data.ratings);
                resolve(res.data.data.rating_result.data.ratings)
            })
            .catch((err) => {
                console.log(err);
                reject([])
            })
    })
};