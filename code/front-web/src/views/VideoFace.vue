<template>
    <div class="container">
        <el-row :gutter="20">
            <el-col :span="12">
                <h2>视频画面</h2>
                <webcam ref="webcam"
                        :device-id="deviceId"
                        width="100%"
                        @started="onStarted"
                        @stopped="onStopped"
                        @error="onError"
                        @cameras="onCameras"
                        @camera-change="onCameraChange">
                </webcam>
                <el-select v-model="camera" placeholder="请选择当前摄像设备">
                    <el-option v-for="device in devices"
                               :key="device.deviceId"
                               :value="device.deviceId"
                               :label="device.label">
                    </el-option>
                </el-select>
                --
                <el-button type="success"
                           icon="el-icon-view"
                           round
                           @click="onStart">启动摄像头
                </el-button>
                <el-button type="warning"
                           round
                           icon="el-icon-circle-close"
                           @click="onStop">停止摄像头
                </el-button>
            </el-col>

            <el-col :span="12">
                <h2>截屏图片</h2>
                <figure class="figure">
                    <img :src="img" class="img-responsive">
                </figure>
                <el-button type="primary"
                           round
                           icon="el-icon-picture"
                           :disabled="btnStatus"
                           @click="onCapture">截屏
                </el-button>
                <el-button type="success"
                           round
                           icon="el-icon-download"
                           @click="onSave">
                </el-button>
            </el-col>

        </el-row>
    </div>
</template>

<script>
    import webcam from '../components/Webcam'
    import {find, head} from "lodash"

    export default {
        name: "VideoFace",
        components: {
            webcam,
        },
        data() {
            return {
                btnStatus: false,
                img: null,
                camera: null,
                deviceId: null,
                devices: []
            };
        },
        computed: {
            device: function () {
                return find(this.devices, n => n.deviceId === this.deviceId);
            },
        },
        watch: {
            camera(id) {
                this.deviceId = id;
            },
            devices() {
                let first = head(this.devices);
                console.log("first: " + first);
                if (first) {
                    this.camera = first.deviceId;
                    this.deviceId = first.deviceId;
                }
            },
        },
        methods: {
            onCapture() {
                this.img = this.$refs.webcam.capture();
            },
            onStarted(stream) {
                console.log("On Started Event", stream);
            },
            onStopped(stream) {
                console.log("On Stopped Event", stream);
            },
            onStop() {
                this.btnStatus = true;
                this.$refs.webcam.stop();
            },
            onStart() {
                this.$refs.webcam.start();
            },
            onError(error) {
                console.log("On Error Event", error);
            },
            onCameras(cameras) {
                this.devices = cameras;
                console.log("On Cameras Event", cameras);
            },
            onCameraChange(deviceId) {
                this.deviceId = deviceId;
                this.camera = deviceId;
                console.log("On Camera Change Event", deviceId);
            },
            onSave() {
                // base64 转 Blob
                let base64ToBlob = function(imgSrc) {
                    let parts = imgSrc.split(';base64,');
                    let contentType = parts[0].split(':')[1];
                    let raw = window.atob(parts[1]);
                    let rawLength = raw.length;
                    let uInt8Array = new Uint8Array(rawLength);
                    for(let i = 0; i < rawLength; ++i) {
                        uInt8Array[i] = raw.charCodeAt(i);
                    }
                    return new Blob([uInt8Array], {
                        type: contentType
                    });
                };
                // 随机文件名生成
                let saveName = function(length, subStr) {
                    return Math.random().toString(length).substr(subStr);
                };

                if (this.img == null) {
                    this.$notify.info({
                        title: '提示',
                        message: '当前没有截取图片或截取图片失败，请重新再试'
                    })
                }
                else {
                    let aTag = document.createElement('a');
                    const pic = this.img;
                    document.body.appendChild(aTag);
                    aTag.style.display = 'none';
                    let blob = base64ToBlob(pic);
                    aTag.download = saveName(4,2);
                    aTag.href = URL.createObjectURL(blob);
                    aTag.click();
                    URL.revokeObjectURL(blob);
                }
            },
        }
    }
</script>

<style scoped>

</style>