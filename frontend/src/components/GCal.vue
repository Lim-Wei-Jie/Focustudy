<template>
    <div class="gcal">
        gcal!

    <span>
    <button type="button" class="btn btn-dark" @click="showEvents()">Get Events</button>
    </span>

    <div v-if="this.events !== null">
        {{this.events}}
        <!-- <div v-for="event in events">
            <div>
                <h3>{{ event.summary }}</h3>
                <p>{{ event.description }}</p>
                <p>{{ event.start.dateTime }}</p>
                <p>{{ event.end.dateTime }}</p>
            </div>
        </div> -->
        
    </div>

    </div>
</template>

<script>
import getEvents from '../endpoint/endpoint.js'

export default {
    name: "GCal",
    data() {
        return {
            events: null,
            show: false
        }
    },

    created() {
        this.events = getEvents()
        console.log(this.events)

        // id = event['id']
        // name = event['summary']
        // start = event['start'] - can be date or datetime
        // end = event['end'] - can be date or datetime
        // link = event['htmlLink']
        // final_events[id] = {'name': name, 'start': start, 'end': end, 'link': link}
    },

    methods: {
        showEvents() {
            this.show = true
        }
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