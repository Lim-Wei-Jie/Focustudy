<template>
    <header>
        <h1>Task List</h1>
        <Button 
            :text="showAddTask ? 'Close' : 'Add Task'"
            :color="showAddTask ? 'red' : 'green'"
            @btn-click="$emit('show-task')"
        />
    </header>
</template>

<script>

import Button from "./Button"

export default {
    name: "Header",
    props: [
        "showAddTask"
    ],
    components: {
        Button
    }
}
</script>

<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
</style>
