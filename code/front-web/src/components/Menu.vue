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
                    { path: 'project', navItem: '2019Sandau 实时人脸检测系统'},
                    // { path: '/video-face', navItem: '实时视频检测'},
                    { path: '/img-face', navItem: '图片检测'},
                    { path: '/about', navItem: '论文&系统简介'},
                    { path: 'thanks', navItem: '致谢'},
                    { path: '/feedback', navItem: '问题&反馈'}
                ]
            }
        }
    }
</script>

<style scoped>

</style>