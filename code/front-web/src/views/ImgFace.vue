<template>
    <div class="imgFace">
        <h1>This is an img page</h1>
        <el-button @click="onTest">test</el-button>
    </div>
</template>

<script>
    export default {
        name: "ImgFace",

        methods: {
            onTest()
            {
                this.$http.get('http://127.0.0.1:5000/test').then(res =>{
                        this.$notify({
                            message: res.data.result,
                            type: 'success'
                        })
                    }
                )
            }
        }
    }
</script>

<style scoped>

</style>