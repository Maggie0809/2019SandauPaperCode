import axios from "axios";
//import qs from "qs";
import {Notification} from 'element-ui';
import router from "../router";

// axios 配置
axios.defaults.timeout = 60000;
axios.defaults.withCredentials = true;

//http request 拦截器
// axios.interceptors.request.use((config) => {
//     return config;
// }, error => {
//     return Promise.reject(error);
// });

export default axios;