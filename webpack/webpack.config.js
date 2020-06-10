const path = require('path');

module.exports = env => {
    const paths = {
        STATIC_JS: path.join(__dirname, '/../', 'static/', 'js/'),
        WEBPACK: path.join(__dirname, '/../', './webpack')
    }
    return {
        "mode": "development",
        "entry": {
            "home": path.resolve(paths.WEBPACK, 'src/home.js'),
        },
        "output": {
            "path": path.resolve(paths.STATIC_JS, 'compiled/'),
            "filename": "[name].[chunkhash:8].js"
        },
        "module": {
            "rules": [
                {
                    "enforce": "pre",
                    "test": /\.(js|jsx)$/,
                    "exclude": /node_modules/,
                    "use": "eslint-loader"
                },
                {
                    "test": /\.(js|jsx)$/,
                    "exclude": /node_modules/,
                    "use": {
                        "loader": "babel-loader",
                        "options": {
                            "presets": [
                                "@babel/preset-env",
                                "@babel/preset-react"
                            ]
                        }
                    }
                },
                {
                    "test": /\.scss$/,
                    "use": [
                        "style-loader",
                        "css-loader",
                        "sass-loader"
                    ]
                },
//                {
//                    "test": /\.tsx?$/,
//                    "exclude": /node_modules/,
//                    "use": {
//                        "loader": "ts-loader",
//                        "options": {
//                            "transpileOnly": true
//                        }
//                    }
//                },
            ]
        }
    }
}