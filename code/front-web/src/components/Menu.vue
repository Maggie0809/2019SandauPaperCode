<template>
    <div>
        <el-menu mode="horizontal" router="true"
                 background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
            <el-menu-item v-for="(item, i) in navList" :key="i" :index="item.path">
                    {{ item.navItem }}
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "Menu",

        data(){
            return {
                navList:[
                    { path: '/', navItem: '2019Sandau webAPI 图片检测'},
                    { path: '/img-face', navItem: '图片检测'},
                    { path: '/about', navItem: '系统简介'},
                ]
            }
        }
    }
</script>

<style scoped>

</style>