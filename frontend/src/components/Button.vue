<template>
    <button 
        @click="clicked()"
        :style="{background: color}"
        class="btn"
    >
        {{text}}
    </button>
</template>

<script>

    export default {
        name: "Button",
        props: [
            "text",
            "color",
        ],
        methods: {
            clicked() {
                this.$emit("btn-click")
            }
        }
    } 
</script>
