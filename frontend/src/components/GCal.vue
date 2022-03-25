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

// import moment from 'moment';

const CLIENT_ID = '574353437454-f7voc61o6o6l9l9itlfc5kf8g96v8c7g.apps.googleusercontent.com';
const API_KEY = 'AIzaSyA8WHBWyTs5a0nhvD_rmbWH5HaFgwhx4hY';
const DISCOVERY_DOCS = ['https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest'];
const SCOPES = 'https://www.googleapis.com/auth/calendar.readonly';

export default {
    name: "GCal",
    data() {
        return {
            // Client ID and API key from the Developer Console
            authorized: false,
            items: undefined,
            api: undefined,
        }
    },

    mounted() {
    },

    created() {
        var gapi = window.gapi
        this.api = gapi;
        this.handleClientLoad();
    },

    methods: {
        handleClientLoad() {
            this.api.load('client:auth2', this.initClient);
        },
    
        initClient() {
            let vm = this;
            vm.api.client.init({
                apiKey: API_KEY,
                clientId: CLIENT_ID,
                discoveryDocs: DISCOVERY_DOCS,
                scope: SCOPES
            }).then(() => {
            vm.api.auth2.getAuthInstance().isSignedIn.listen(vm.authorized);
            });
        },

        handleAuthClick() {
            Promise.resolve(this.api.auth2.getAuthInstance().signIn())
                .then(() => {
                    this.authorized = true;
                });
        },
        handleSignOutClick() {
            Promise.resolve(this.api.auth2.getAuthInstance().signOut())
                .then(() => {
                    this.authorized = false;
                });
        },
        getEvents() {
            let vm = this;
            vm.api.client.calendar.events.list({
                'calendarId': 'primary',
                'timeMin': 'YYYY-MM-DDTHH:mm:ss.SZ',
                'timeMax': 'YYYY-MM-DDTHH:mm:ss.SZ)',
                'showDeleted': false,
                'singleEvents': true,
                'maxResults': 10,
                'orderBy': 'startTime'
            }).then(response => {
                this.items =  response.result.items;
            });
        },
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