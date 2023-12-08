"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  name: "showTHistoryList",
  data() {
    return {};
  },
  props: {
    HistoryList: {
      type: Object
    },
    classnumber: {
      type: String
    }
  },
  methods: {
    updateIsFlag() {
      this.$emit("updateIsFlag", -1);
    }
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
    c: common_vendor.t($props.classnumber),
    d: common_vendor.f($props.HistoryList, (item, index, i0) => {
      return {
        a: common_vendor.t(item.time),
        b: common_vendor.t(item.checkinNumber),
        c: common_vendor.t(item.uncheckinNumber),
        d: index
      };
    })
  };
}
const Component = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "C:/Users/86198/Desktop/小程序/SginInSystem/components/showTHistoryList/showTHistoryList.vue"]]);
wx.createComponent(Component);
