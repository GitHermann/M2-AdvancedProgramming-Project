<template>
    <div class="button-container">
        <button class="button">
            <i class="icon"></i>
            <span class="text">Button 1</span>
        </button>
        <button class="button">
            <i class="icon"></i>
            <span class="text">Button 2</span>
        </button>
        <button class="button">
            <i class="icon"></i>
            <span class="text">Button 3</span>
        </button>
        <button class="button">
            <i class="icon"></i>
            <span class="text">Button 4</span>
        </button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            message: 'Hello, Vue!'
        }
    },
    methods: {
        showMessage() {
            alert(this.message);
        }
    }
}
</script>

<style scoped>
.button-container {
    width: 200px;
    height: 400px;
    display: flex;
    flex-direction: column;
}

.button {
    display: flex;
    align-items: center;
    padding: 10px;
    margin-bottom: 10px;
    background-color: #f0f0f0;
    border: none;
    border-radius: 5px;
}

.icon {
    margin-right: 10px;
}

.text {
    font-size: 14px;
}
</style>
