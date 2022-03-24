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

                            <button type="submit" class="btn btn-success" @click="catchd">Exit</button>
                            <button type="submit" class="btn btn-danger" @click="gethd">Get data</button>
                    
                        </div>
                    
                </div>
        </div>
    </div>

    <div class="container">

        
        <h3 class="p-3 text-center">Vue.js - Display a list of items with v-for</h3>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Role</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in users" :key="user.id">
                    <td>{{user.firstName}} {{user.lastName}}</td>
                    <td>{{user.email}}</td>
                    <td>{{user.role}}</td>
                </tr>
            </tbody>
        </table>
    </div>  

</div>







       
</template>


<script>



import {catchRate} from "../endpoint/endpoint.js"
import {getRate} from "../endpoint/endpoint.js"

export default {
    name: 'Rating',
    data() {
    return {
      picked: null,
      email:"haha@gmail.com",
      toggle: true,
      toggle2: false,
      userdata:"2",
      users: [
                { firstName: 'Frank', lastName: 'Murphy', email: 'frank.murphy@test.com', role: 'User' },
                { firstName: 'Vic', lastName: 'Reynolds', email: 'vic.reynolds@test.com', role: 'Admin' },
                { firstName: 'Gina', lastName: 'Jabowski', email: 'gina.jabowski@test.com', role: 'Admin' },
                { firstName: 'Jessi', lastName: 'Glaser', email: 'jessi.glaser@test.com', role: 'User' },
                { firstName: 'Jay', lastName: 'Bilzerian', email: 'jay.bilzerian@test.com', role: 'User' }
            ]
    }
  },

  methods: {
    

    // Called when clicked
    catchd() {
      // Add new record to rating database


      console.log(this.picked)
    
        catchRate({
          "productivity": this.picked,
          "email": this.email
        })
    },


    gethd() {
      // get record from database


        this.userdata = getRate()
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