<template>
  <div class="gcal">
      gcal!
    <!-- <button id="authorize_button">Authorize</button>
    <button id="signout_button">Sign Out</button> -->
    <button type="button" class="btn btn-primary"  v-if="!authorized" @click="handleAuthClick">Login</button> 
    <button type="button" class="btn btn-primary" v-if="authorized" @click="handleSignOutClick">Sign Out</button>
    <button type="button" class="btn btn-primary" v-if="authorized" @click="getEvents">Get Events</button>

  </div>
</template>

<script>
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
        }
    },

    mounted() {
    let Script = document.createElement("script");
    Script.setAttribute("src", "https://apis.google.com/js/platform.js?onload=onLoadCallback");
    document.head.appendChild(Script);
    },

    created() {
        this.api = gapi;
        this.handleClientLoad();

        window.onLoadCallback = function(){
        gapi.auth2.init({
        client_id: CLIENT_ID
        });
    }
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
            }).then(_ => {
            vm.api.auth2.getAuthInstance().isSignedIn.listen(vm.authorized);
            });
        },

        handleAuthClick(event) {
            Promise.resolve(this.api.auth2.getAuthInstance().signIn())
                .then(_ => {
                    this.authorized = true;
                });
        },
        handleSignOutClick(event) {
            Promise.resolve(this.api.auth2.getAuthInstance().signOut())
                .then(_ => {
                    this.authorized = false;
                });
        },
        getEvents() {
            let vm = this;
            vm.api.client.calendar.events.list({
                'calendarId': 'primary',
                'timeMin': (moment(this.filters.start).format('YYYY-MM-DDTHH:mm:ss.SZ')),
                'timeMax': (moment(this.filters.end).format('YYYY-MM-DDTHH:mm:ss.SZ')),
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

<style>
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
</style>