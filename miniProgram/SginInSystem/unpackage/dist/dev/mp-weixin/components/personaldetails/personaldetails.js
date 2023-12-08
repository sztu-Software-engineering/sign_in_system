"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  name: "personaldetails",
  data() {
    return {
      isInputDialogVisible: false,
      inputValue: ""
    };
  },
  methods: {
    openInputDialog() {
      this.isInputDialogVisible = true;
      console.log(this.isInputDialogVisible);
    },
    confirmInputDialog() {
      const pattern = /^\d{5}$/;
      if (!pattern.test(this.inputValue)) {
        common_vendor.index.showToast({
          title: "课程号错误！",
          icon: "error",
          duration: 2e3
          //持续时间为 2秒
        });
      } else {
        this.isInputDialogVisible = false;
      }
      this.inputValue = "";
    },
    cancelInputDialog() {
      console.log(this.isInputDialogVisible);
      this.isInputDialogVisible = false;
      this.inputValue = "";
    }
  }
};
if (!Array) {
  const _easycom_uni_card2 = common_vendor.resolveComponent("uni-card");
  _easycom_uni_card2();
}
const _easycom_uni_card = () => "../../uni_modules/uni-card/components/uni-card/uni-card.js";
if (!Math) {
  _easycom_uni_card();
}
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return {
    a: common_vendor.o((...args) => $options.openInputDialog && $options.openInputDialog(...args)),
    b: $data.inputValue,
    c: common_vendor.o(($event) => $data.inputValue = $event.detail.value),
    d: common_vendor.o((...args) => $options.cancelInputDialog && $options.cancelInputDialog(...args)),
    e: common_vendor.o((...args) => $options.confirmInputDialog && $options.confirmInputDialog(...args)),
    f: $data.isInputDialogVisible
  };
}
const Component = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "C:/Users/86198/Desktop/小程序/SginInSystem/components/personaldetails/personaldetails.vue"]]);
wx.createComponent(Component);
