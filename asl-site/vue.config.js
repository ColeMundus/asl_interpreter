{
  {
    [
      {
        test: /\.pug$/,
        loader: "pug-plain-loader"
      }
    ];
  }
}
const path = require("path");

module.exports = {
  pluginOptions: {
    "style-resources-loader": {
      preProcessor: "scss",
      patterns: [path.resolve(__dirname, "./src/styles/_global.scss")]
    }
  },
  devServer: {
    host: "0.0.0.0",
    disableHostCheck: true
  }
};
