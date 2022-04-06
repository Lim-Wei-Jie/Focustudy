<template>
    <div class="spotify text-center text-light">
        <img src="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_CMYK_White.png" width="100" class="mb-4"/>
        <br>
        <button class="btn btn-sm btn-light bg-success text-light rounded m-2 px-3" @click="getSongs()">Show My Top Tracks</button>
        <br>
        <button class="btn btn-sm btn-light bg-success text-light rounded m-2 px-3" @click="getPlaylists()">Select A Playlist</button>

        <div id="playlist" v-if="showPlaylists" class="m-2">
            <select class="form-select" v-model="selected" @change="getSelected()">
                <option v-for="playlist in displayPlaylists" :key="playlist.name" :value="playlist.uri">{{playlist.name}}</option>
            </select>
        </div>

        <div v-if="showTopTracks">
            <div v-for="track in displayTracks" :key="track.id"> 
                <iframe class="iframe-track" allowtransparency="true"
                :src="track.id"
                allow="encrypted-media" frameborder="0"></iframe>
            </div>
        </div>

        <div v-if="showSelectedTracks">
            <div v-for="track in displayChosenTracks" :key="track.id"> 
                <iframe class="iframe-track" allowtransparency="true"
                :src="track.id"
                allow="encrypted-media" frameborder="0"></iframe>
            </div>
        </div>
        
    </div>
</template>


<script>

import { getAllPlaylists, getTopTracks, getChosenPlaylist } from '../endpoint/endpoint.js'

export default {
    name: "Spotify",
    data() {
        return {
            tracks: {},
            playlists: {},
            playlistTracks: {},

            displayTracks: [],
            displayPlaylists: [],
            displayChosenTracks: [],

            selected: '',

            show: true,
            showPlaylists: false,
            showTopTracks: false,
            showSelectedPlaylists: false,
            showSelectedTracks: false
        }
    },

    created() {
        this.tracks = getTopTracks()
        console.log(this.tracks)

        this.playlists = getAllPlaylists()
        console.log(this.playlists)

        this.chosenPlaylist = getChosenPlaylist()
        console.log(this.chosenPlaylist)
    },

    methods: {  

        getSongs() {
            console.log("getting top tracks")

            this.tracks
            .then((response) => {
                var songs_details = response.tracks.items
                var collected = []

                for (let song in songs_details){
                    // console.log(songs_details[song].uri)
                    let indiv_uri = songs_details[song].id
                    collected.push({id: "https://open.spotify.com/embed/track/"+indiv_uri})
                }

                console.log(collected)
                this.displayTracks = collected
                this.showTopTracks = true
                this.showPlaylists = false
            })
        },

        getPlaylists() {
            this.showPlaylists = true
            console.log("getting playlists")
            console.log(this.playlists)
            this.playlists
            .then((response) => {
                var playlists_details = response.tracks.items
                var collected = []

                for (let playlist in playlists_details){
                    // console.log(playlists_details[playlist])
                    let indiv_uri = playlists_details[playlist].id
                    let indiv_name = playlists_details[playlist].name
                    // console.log(indiv_uri)
                    // console.log(indiv_name) 
                    collected.push({name: indiv_name, uri: indiv_uri})
                }

                console.log(collected)
                this.displayPlaylists = collected
                // this.show = false

            })
        },

        getSelected() {
            this.showTopTracks = false

            console.log(this.selected)
            console.log(typeof(this.selected))
            getChosenPlaylist(this.selected.slice()) 
            // console.log("getting chosen playlist")
            // this.chosenPlaylist
            .then((response) => {
                var songs_details = response.tracks.tracks.items
                var collected = []

                for (let song in songs_details){
                    console.log(songs_details[song])
                    // console.log(songs_details[song].track)
                    let indiv_uri = songs_details[song].track.id
                    // console.log(indiv_uri)
                    collected.push({id: "https://open.spotify.com/embed/track/"+indiv_uri})
                }

                console.log("selected playlist")
                console.log(collected)
                this.displayChosenTracks = collected
                this.showSelectedTracks = true
                // this.show = false

            })
        }}
    }

</script>

<style scoped>
.spotify {
    background-color: black;
    width: 375px;
    margin: 30px auto;
    overflow: scroll;
    height: 300px;
    /* border: 1px solid steelblue; */
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0.5px 5px 10px 12px #E4E4E4;
}

/* width */
::-webkit-scrollbar {
  width: 5px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: green;
  border-radius: 5px;
}

::-webkit-scrollbar-corner {
    display: none;
}

</style>
