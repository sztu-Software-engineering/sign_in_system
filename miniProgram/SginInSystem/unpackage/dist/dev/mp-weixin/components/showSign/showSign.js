"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  name: "showSign",
  data() {
    return {
      Captcha: "-1"
    };
  },
  props: {
    // 接收来自父组件的课程数据
    courses: {
      type: Object,
      default: () => []
    },
    checkInNumber: {
      type: Object
    }
  },
  methods: {
    updateIsFlag() {
      this.$emit("updateIsFlag", -1);
    }
  },
  mounted() {
    this.Captcha = this.courses.classCaptcha;
  }
};
if (!Array) {
  const _easycom_uni_icons2 = common_vendor.resolveComponent("uni-icons");
  _easycom_uni_icons2();
}
const _easycom_uni_icons = () => "../../uni_modules/uni-icons/components/uni-icons/uni-icons.js";
if (!Math) {
  _easycom_uni_icons();
}
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return {
    a: common_vendor.o(($event) => $options.updateIsFlag()),
    b: common_vendor.p({
      type: "back",
      size: "30"
    }),
    c: common_vendor.t($data.Captcha),
    d: common_vendor.t($props.checkInNumber.checkinNumber),
    e: common_vendor.t($props.checkInNumber.uncheckinNumber)
  };
}
const Component = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "C:/Users/86198/Desktop/小程序/SginInSystem/components/showSign/showSign.vue"]]);
wx.createComponent(Component);
