<template>
    <div class="spotify text-center text-light">
        <img src="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_CMYK_White.png" width="100" class="mb-4"/>
        <br>
        <button v-if="show" class="btn btn-sm btn-success rounded mt-5 px-3" @click="getSongs()"><fa icon="play" /></button>
    
        <div v-for="track in display" :key="track.id"> 
            <iframe class="iframe-track" allowtransparency="true"
            :src="track.id"
            allow="encrypted-media" frameborder="0"></iframe>
        </div>
        
    </div>
</template>


<script>

import { getTopTracks } from '../endpoint/endpoint.js'

export default {
    name: "Spotify",
    data() {
        return {
            tracks: {},
            show: true,
            display: [],
        }
    },

    created() {
        this.tracks = getTopTracks()
        console.log(this.tracks)
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
                this.show = false

            })
        },
    }
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
