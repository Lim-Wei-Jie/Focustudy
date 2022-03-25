<template>


<div>

    <div v-show='toggle'>
        <div class="d-flex justify-content-center text-center">
            <div class="card" style="width: 68rem;">
                <div class="card-body">
                    <h5 class="card-title">How was your study session today?</h5>
                    <div class="container">
                        <div class="starrating risingstar d-flex justify-content-center flex-row-reverse">
                            <input type="radio" id="star5" name="rating" value="5" v-model="picked" @click='toggle = !toggle'/><label for="star5" title="5 star">5</label>
                            <input type="radio" id="star4" name="rating" value="4" v-model="picked" @click='toggle = !toggle'/><label for="star4" title="4 star">4</label>
                            <input type="radio" id="star3" name="rating" value="3" v-model="picked" @click='toggle = !toggle'/><label for="star3" title="3 star">3</label>
                            <input type="radio" id="star2" name="rating" value="2" v-model="picked" @click='toggle = !toggle'/><label for="star2" title="2 star">2</label>
                            <input type="radio" id="star1" name="rating" value="1" v-model="picked" @click='toggle = !toggle'/><label for="star1" title="1 star">1</label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <div v-show='!toggle'>
        <div class="d-flex justify-content-center">
                <div class="content text-center">
                   
                        <div class="ratings"> <h2>You rated:</h2> <span class="product-rating">{{picked}}</span><span>/5</span>
                            <div class="rating-text"> <span>Thank you for using FocusStudy</span> </div>

                            <button type="submit" class="btn btn-success" @click="currentDate() ; classifytime(this.currenTime); catchd();">Exit</button>
                            <button type="submit" class="btn btn-danger" @click="gethd(); calculateAverage(); ">Get data</button>
                    
                        </div>
                    
                </div>
        </div>
    </div>

    

    <div class="container">
        {{this.avgMorningGpa}}
        {{this.avgAfternoonGpa}}
        {{this.avgNightGpa}}
        <h3 class="p-3 text-center">Rating table</h3>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>Morning</th>
                    <th>Afternoon</th>
                    <th>Night</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{{this.avgMorningGpa}} </td>
                    <td>{{this.avgAfternoonGpa}}</td>
                    <td>{{this.avgNightGpa}}</td>
                    
                </tr>
            </tbody>
        </table>
    </div>  

</div>







       
</template>


<script>


//import something from "../endpoint/endpoint.js"

import {catchRate} from "../endpoint/endpoint.js"
import axios from "axios";
let url = "http://127.0.0.1:5000/getRating"



export default {
    name: 'Rating',
    data() {
    return {
      picked: null,
      email:"haha@gmail.com",
      toggle: true,
      toggle2: false,
      userdata:[],
      currentdate:"",
      currenTime:"",
      partDay:"",
      nightGPA:0,
      morningGPA:0,
      afternoonGPA:0,
      extralist:[],
      morningGPAList:[],
      afternoonGPAList:[],
      nightGPAList:[],
      avgMorningGpa:0,
      avgAfternoonGpa:0,
      avgNightGpa:0
      
     
    }
  },

  methods: {




    // Called when clicked
    catchd() {
      // Add new record to rating database


    
        catchRate({
          "productivity": this.picked,
          "email": this.email,
          "currentDate": this.currentdate,
          "partDay": this.partDay,
          "morningGPA": this.morningGPA,
          "afternoonGPA": this.afternoonGPA,
          "nightGPA":this.nightGPA
        })


        


        
    },

   




    gethd() {
      // get record from database

      axios.get(url).then(response => {
            this.results = response.data
            console.log(response.data)
            this.userdata =response.data.data.ratings 
            console.log(this.userdata)




             for (const [key1, value1] of Object.entries(this.userdata)) {

                    console.log({key1})

                    for (const [key, value] of Object.entries(value1))
                    {
                        //console.log(`${key}`);
                        if (`${key}` == "morningGPA" )
                        {
                            //console.log('here')
                            //console.log('hahaha')
                            this.morningGPAList.push(Number(`${value}`))
                        }
                    }
                    
                    }
        
                //console.log(this.morningGPAList)


                

                this.avgMorningGpa = 0;
                var total = 0;
                //this.morningGPAList=[]

                for(var j = 0; j < this.morningGPAList.length; j++) {
                   total += Number(this.morningGPAList[j]);
                }
                this.avgMorningGpa = total / this.morningGPAList.length;
                //console.log(total)







           



                    //this.morningGPAList = this.extralist







                    

            
          })

       
         //this.morningGPAList.push(this.picked)

         
         

       
    },

    

    currentDate() {
      const current = new Date();
      const date = `${current.getDate()}/${current.getMonth()+1}/${current.getFullYear()}`;
      const time = current.getHours()
      this.currentdate = date
      this.currenTime = time
      console.log(this.currenTime)
      
    },
    
    classifytime(x) {
    if ((x >= 0) && (x <= 12)){
        this.partDay = 'Morning'
        this.morningGPA = this.picked
        //this.morningGPAList.push(this.picked)
        console.log(this.morningGPAList)
        return 'Morning'
    } else if ((x > 12) && (x <= 18 )){
        this.partDay = 'Afternoon'
        return 'Afternoon'
    } else {
        this.partDay = 'Night'
        console.log("Night")
        return 'Night'
    }
    
    },


    calculateAverage() {


        

         

        if (this.partDay == "Morning")
        
        {
            
            //console.log(this.morningGPAList)


   

            
            
            //this.avgMorningGpa = 32
            //console.log(this.avgMorningGpa)
            //console.log(44)

        }

        


        if (this.partDay == "Afternoon")
        {

            this.avgAfternoongGpa = 0;
            for(var j = 0; j < this.afternoonGPAList.length; j++) {
                //total += Number(this.afternoonGPAList[j]);
            }
            //this.avgafternoonGpa = total / this.afternoonGPAList.length;
            //console.log(total)

        }


        if (this.partDay == "Night")
        {

            this.avgNightGpa = 0;
            for(var z = 0; z < this.nightGPAList.length; z++) {
                //total += Number(this.afternoonGPAList[z]);
            }
            //this.avgNightGpa = total / this.nightGPAList.length;
            //console.log(total)

        }
        

                    //console.log(this.nightGPA)
       
    }

    

  }
  

}



</script>
<style scoped>

@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);
@import url(//fonts.googleapis.com/css?family=Open+Sans&display=swap);


/* Styling h1 and links
––––––––––––––––––––––––––––––––– */
h1[alt="Simple"] {color: white;}
a[href], a[href]:hover {color: grey; font-size: 0.5em; text-decoration: none}


body
{
  background: #4a4a4c !important;
}

.starrating > input {display: none;}  /* Remove radio buttons */

.starrating > label:before { 
  content: "\f005"; /* Star */
  margin: 2px;
  font-size: 8em;
  font-family: FontAwesome;
  display: inline-block; 
}

.starrating > label
{
  color: #222222; /* Start color when not clicked */
}

.starrating > input:checked ~ label
{ color: #ffca08 ; } /* Set yellow color when star checked */

.starrating > input:hover ~ label
{ color: #ffca08 ;  } /* Set yellow color when star hover */

 body {
     margin: 0;
     padding: 0;
     font-family: 'Open Sans', serif;
     background: #eee
 }

 .content {
     width: 420px;
     margin-top: 100px
 }

 .ratings {
     background-color: #fff;
     padding: 54px;
     border: 1px solid rgba(0, 0, 0, 0.1);
     box-shadow: 0px 10px 10px #E0E0E0
 }

 .product-rating {
     font-size: 50px
 }

 .stars i {
     font-size: 18px;
     color: #28a745
 }

 .rating-text {
     margin-top: 10px
 }



</style>