<template>

    <div @click="$emit('toggle-reminder', task.task_id)" :class="[task.reminder ? 'reminder' : '', 'task']">
        <p class="align-left">
            <i @click="strikethrough" class="tick fa-solid fa-check fa-lg"></i>
            <span style="padding-left: 10px;" :style="{textDecoration: striked ? 'line-through' : ''}">
                {{ task.task_description }}
            </span>
        </p>
        <p class="align-right">
            <i @click="$emit('delete-task', task.task_id)" class="fas fa-times fa-lg"></i>
        </p>
        <!-- <br> -->
        <!-- <p v-if="task.day!=''" class="align-left">
            {{ task.day }}
        </p> -->
    </div>

</template>

<script>

export default {
    name: "Task",
    props: [
        "task"
    ],
    data() {
        return {
            striked: false,
        };
    },
    methods: {
        strikethrough() {
            this.striked = !this.striked
        }
    }
}

</script>

<style >
    .tick {
        color: rgb(3,54,49);
    }
    .fas {
        color: #ECA742;
    }

    .task {
        /* background: #f4f4f4; */
        margin: 10px;
        padding: 15px 10px;
        /* cursor: pointer; */
    }
    /* .task.reminder {
        border-left: 5px solid green;
    }
    .task h3 {
        display: flex;
        align-items: center;
        justify-content: space-between;
    } */
    .align-right {
        float: right;
    }
    .align-left {
        float: left
    }
</style>