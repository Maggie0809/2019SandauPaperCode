var path = require('path')

module.exports = {
    dev: {
        env: require('./dev.env'),
        port: 2333,
        // autoOpenBrowser: true,
        assetsSubDirectory: 'static',
        assetsPublicPath: '/',
        proxyTable: {
            '/api': {
                target: 'http://localhost:5000',
                changeOrigin: true,
                // pathRewrite: {
                //     '^/api': ''
                // }
            }
        },
        // CSS Sourcemaps off by default because relative paths are "buggy"
        // with this option, according to the CSS-Loader README
        // (https://github.com/webpack/css-loader#sourcemaps)
        // In our experience, they generally work as expected,
        // just be aware of this issue when enabling this option.
        cssSourceMap: false
    }
}