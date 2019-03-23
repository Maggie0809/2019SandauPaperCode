<template>
    <div id="app">
        <!--<div id="nav">-->
        <!--<router-link to="/">Home</router-link>-->
        <!--|-->
        <!--<router-link to="/about">About</router-link>-->
        <!--|-->
        <!--<router-link to="/img-face">Img Detection</router-link>-->
        <!--|-->
        <!--<router-link to="/video-face">Video Detection</router-link>-->
        <!--<router-link to="/menu">Menu</router-link>-->
        <!--</div>-->
        <Menu></Menu>
        <router-view/>
    </div>
</template>

<script>
    import Menu from './components/Menu'

    export default {
        name: 'app',
        components: {
            Menu,
        },
        //计算属性
        computed: {
            // ...mapGetters({
            //     sidebar: 'sidebar',
            //     breadcrumbItems: 'breadcrumbItems',
            // })
        },
        data() {
            return {}
        },
        methods: {},
        beforeMount() {
        },
        mounted() {
        },
        beforeCreate() {
        },
        created() {
        }
    }

</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    #nav {
        padding: 30px;
    }

    #nav a {
        font-weight: bold;
        color: #2c3e50;
    }

    #nav a.router-link-exact-active {
        color: #42b983;
    }
</style>
