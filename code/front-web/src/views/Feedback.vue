<template>
    <div>
        <h1>This is Feedback Page.</h1>
        <h2>下面留下您的问题和反馈吧！(使用markdown语法)</h2>

        <mark-down :toolbar="print=true"/>
    </div>

</template>

<script>
    import MarkDown from 'vue-meditor'

    export default {
        name: "Feedback",
        components:{
            MarkDown,
        },

    }
</script>

<style scoped>

</style>