<template>
    <div class="spotify text-center" style="color:white">
        <div v-if="show" style="color:white">
            <button class="btn btn-light m-2 mb-4" @click="getSongs()">Show My Music</button>
            <!-- hello -->
            <!-- {{this.tracks}} -->
            <!-- {{this.display}} -->
        </div>
    
    <div v-for="track in display" :key="track.id"> 
        <iframe class="iframe-track" allowtransparency="true"
        :src="track.id"
        allow="encrypted-media" frameborder="0"></iframe>
    </div>
        
    </div>
</template>


<script>

import getTopTracks from '../endpoint/spotify.js'

export default {
    name: "Spotify",
    data() {
        return {
            tracks: {},
            show: false,
            display: [],
        }
    },

    created() {
        this.tracks = getTopTracks()
        console.log(this.tracks)
        this.show = true
    },

    methods: {  

        getSongs() {
            console.log("pressed button")

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
                this.display = collected

                // this.$store.commit("updateSpotify",
                //                     {collected})

                // this.display = this.$store.state.spotify
                // console.log(this.display)
                // return collected
                // error, cannot access this.display
                // this.display = collected
            })
        },
    }
}
</script>

<style scoped>
.spotify {
    background-color: black;
    max-width: 500px;
    margin: 30px auto;
    overflow: auto;
    min-height: 50px;
    /* border: 1px solid steelblue; */
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0.5px 5px 10px 12px #E4E4E4;
}

</style>
