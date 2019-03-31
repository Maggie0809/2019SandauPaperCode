<template>
    <div class="grid">
        <hr/>
        <el-row>
            <el-col :span="12">
                <el-upload
                        :action="upURL"
                        :auto-upload="auto_up"
                        :limit="num"
                        :multiple="mul"
                        ref="upload"
                        list-type="picture-card"
                        :on-preview="handlePictureCardPreview"
                        :on-error="handError"
                        :on-success="handSuccess"
                        :before-upload="beforeImgUpload">
                    <i class="el-icon-plus"></i>
                </el-upload>
                <hr width="60%">
                <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传图片服务器
                </el-button>
            </el-col>

            <el-col :span="12">
                <el-table :data="token_url" stripe>
                    <el-table-column prop="filename" label="文件名称"></el-table-column>
                    <el-table-column prop="token" label="对应url"></el-table-column>
                    <el-table-column fixed="right" label="操作" width="80px">
                        <template slot-scope="scope">
                            <el-button @click="handleClick(scope.row)"
                                       type="text"
                                       size="small">检测
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-col>
        </el-row>
        <div v-if="resultVisibility" >
            <hr/>
            <p>检测结果</p>
            <P>共有人脸数: {{ face_count }},以下为具体信息</P>
            <el-card v-for="(item, index) in jsonSource"
                     :key="index"
                     style="padding: 3px 0;width: 30%;float: left"
                     type="text"
                     shadow="hover">
                <p>face No.{{index+1}} info:</p>
                <div v-for="(d,idx) in item" :key="idx">
                    {{idx}}--{{d}}
                </div>
            </el-card>
        </div>

    </div>
</template>

<script>
    export default {
        name: "ImgFace",
        components: {},
        data() {
            return {
                upURL: 'http://127.0.0.1:5000/api/upload',
                dialogImageUrl: '',
                dialogVisible: false,
                num: 1,
                auto_up: false,
                mul: true,
                token_url: [],
                jsonSource: '',
                face_count: '',
                resultVisibility: false,
                activeName: '1'
            };
        },
        methods: {
            handlePictureCardPreview(file) {
                this.dialogImageUrl = file.url;
                this.dialogVisible = true;
            },
            handError(file, error, fileList) {
                this.$notify.error({
                    title: "上传失败！",
                    message: '网络或服务器错，请稍后再试。'
                });
                console.log(file, error, fileList);
            },
            // handRemove(file, fileList){
            //     this.jsonSource = '';
            //     console.log(fileList,file)
            // },
            handSuccess(response) {
                let msg = response.message;
                this.$notify.success({
                    title: 'Success',
                    message: msg
                });

                this.token_url.push(response)
            },
            beforeImgUpload(file) {
                const isJPG = file.type === 'image/jpeg';
                const isLt2M = file.size / 1024 / 1024 < 2;
                if (!isJPG) {
                    this.$message.error('上传图片只能是 JPG 格式!');
                } else if (!isLt2M) {
                    this.$message.error('上传图片大小不能超过 2MB!');
                }
                return isJPG && isLt2M;
            },
            submitUpload() {
                this.$refs.upload.submit()
            },
            handleClick(row) {
                const url = "http://127.0.0.1:5000" + row.token;

                this.$http.get(url).then(res => {
                    if (res.data.hasOwnProperty("count")) {
                        console.log(res);
                        this.face_count = res.data.count;
                        this.jsonSource = res.data.face_data;
                        this.resultVisibility = true;
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .grid {
        margin-bottom: 10px
    }

    .tree-view-item {
        font-family: monospace;
        font-size: 14px;
        margin-left: 18px;
    }

    .tree-view-wrapper {
        overflow: auto;
    }

    /* Find the first nested node and override the indentation */
    .tree-view-item-root > .tree-view-item-leaf > .tree-view-item {
        margin-left: 0;
    }

    /* Root node should not be indented */
    .tree-view-item-root {
        margin-left: 0;
    }

    .tree-view-item-node {
        cursor: pointer;
        position: relative;
        white-space: nowrap;
    }

    .tree-view-item-leaf {
        white-space: nowrap;
    }

    .tree-view-item-key {
        font-weight: bold;
    }

    .tree-view-item-key-with-chevron {
        padding-left: 14px;
    }


    .tree-view-item-key-with-chevron.opened::before {
        top: 4px;
        transform: rotate(90deg);
        -webkit-transform: rotate(90deg);
    }

    .tree-view-item-key-with-chevron::before {
        color: #444;
        content: '\25b6';
        font-size: 10px;
        left: 1px;
        position: absolute;
        top: 3px;
        transition: -webkit-transform .1s ease;
        transition: transform .1s ease;
        transition: transform .1s ease, -webkit-transform .1s ease;
        -webkit-transition: -webkit-transform .1s ease;
    }

    .tree-view-item-hint {
        color: #ccc
    }
</style>