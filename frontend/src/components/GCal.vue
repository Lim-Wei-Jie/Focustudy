<template>
    <div class="gcal">
        gcal!
    <!-- <button id="authorize_button">Authorize</button>
    <button id="signout_button">Sign Out</button> -->
    <span>
        <button type="button" class="btn btn-dark"  v-if="!authorized" @click="handleAuthClick">Login</button> 
    </span>

    <span>
    <button type="button" class="btn btn-dark" v-if="authorized" @click="handleSignOutClick">Sign Out</button>
    </span>

    <span>
    <button type="button" class="btn btn-dark" v-if="authorized" @click="getEvents">Get Events</button>
    </span>

    </div>
</template>

<script>
export default {
    name: "GCal",
    data() {
        return {
            
        }
    },

    mounted() {
    },

    created() {
    },

    methods: {
    }

}
</script>

<style scoped>
.gcal {
    max-width: 500px;
    margin: 30px auto;
    overflow: auto;
    min-height: 300px;
    /* border: 1px solid steelblue; */
    padding: 30px;
    border-radius: 20px;
    background: #F7F8F7;
    box-shadow: 0.5px 5px 10px 12px #E4E4E4;
}

.btn {
    margin: 10px;
}
</style>