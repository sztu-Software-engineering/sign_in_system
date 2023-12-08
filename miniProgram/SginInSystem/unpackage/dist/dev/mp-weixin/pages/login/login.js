"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  data() {
    return {
      Authentication: 0
      //身份认证，0为学生，1为老师
    };
  },
  onShow() {
    common_vendor.index.hideHomeButton();
  }
};
if (!Array) {
  const _easycom_Login2 = common_vendor.resolveComponent("Login");
  _easycom_Login2();
}
const _easycom_Login = () => "../../components/Login/Login.js";
if (!Math) {
  _easycom_Login();
}
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return {};
}
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "C:/Users/86198/Desktop/小程序/SginInSystem/pages/login/login.vue"]]);
wx.createPage(MiniProgramPage);
