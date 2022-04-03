<template>
    <div class="spotify" style="color:white">
        spotify!
    </div>
</template>


<script>

import getTopTracks from '../endpoint/spotify.js'

export default {
    name: "Spotify",
    data() {
        return {
            tracks: null,
            show: false
        }
    },

    created() {
        this.tracks = getTopTracks()
        console.log(this.tracks)
        },
    }

</script>

<style scoped>
.spotify {
    background-color: black;
    max-width: 500px;
    margin: 30px auto;
    overflow: auto;
    min-height: 300px;
    /* border: 1px solid steelblue; */
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0.5px 5px 10px 12px #E4E4E4;
}

</style>
