"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  name: "handSign",
  data() {
    return {
      focus: true,
      //input焦点，用于键盘隐藏后重新唤起
      // 验证码框颜色
      codeclolor: "#313131",
      //自定义光标的颜色
      code: "",
      //这是用户输入的验证码
      isWithinTime: false
    };
  },
  props: {
    // 接收来自父组件的课程数据
    courses: {
      type: Object,
      default: () => []
    }
  },
  methods: {
    updateIsFlag() {
      this.$emit("updateIsFlag", -1);
    },
    // 输入验证码
    codenum: function(event) {
      var that = this;
      var code = event.target.value;
      that.code = code;
      if (code.length === 6) {
        const startTime = this.courses.signinTime;
        console.log(startTime);
        const currentTime = (/* @__PURE__ */ new Date()).getTime();
        console.log(currentTime);
        const isWithinTime = currentTime - startTime < 60 * 3 * 1e3;
        if (isWithinTime) {
          if (code === this.courses.classCaptcha) {
            common_vendor.index.showToast({
              title: "签到成功！",
              icon: "success",
              //将值设置为 success 或者 ''
              duration: 2e3
              //持续时间为 2秒
            });
            setTimeout(function() {
              that.updateIsFlag();
            }, 2e3);
          } else {
            that.codeclolor = "#ff0000";
            setTimeout(function() {
              that.code = "";
              event.target.value = "";
              that.codeclolor = "#313131";
            }, 1e3);
          }
        } else {
          common_vendor.index.showToast({
            title: "超过签到时间！",
            icon: "error",
            duration: 2e3
            //持续时间为 2秒
          });
          setTimeout(function() {
            that.updateIsFlag();
          }, 2e3);
        }
      }
    },
    // 键盘隐藏后设置失去焦点
    blur: function() {
      var that = this;
      that.focus = false;
    },
    // 点击自定义光标显示键盘
    codefocus: function(e) {
      var that = this;
      if (e == that.code.length) {
        that.focus = true;
      }
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
  return common_vendor.e({
    a: common_vendor.o(($event) => $options.updateIsFlag()),
    b: common_vendor.p({
      type: "back",
      size: "30"
    }),
    c: $data.codeclolor == "#ff0000"
  }, $data.codeclolor == "#ff0000" ? {} : {}, {
    d: common_vendor.o((...args) => $options.blur && $options.blur(...args)),
    e: common_vendor.o([($event) => $data.code = $event.detail.value, (...args) => $options.codenum && $options.codenum(...args)]),
    f: $data.focus,
    g: $data.code,
    h: common_vendor.f(6, (item, index, i0) => {
      return {
        a: common_vendor.t($data.code[index]),
        b: index,
        c: common_vendor.o(($event) => $options.codefocus(index), index),
        d: common_vendor.s(index == $data.code.length ? "border: 5rpx solid #1195db;width: 80rpx;height: 80rpx;line-height: 80rpx;" : "color: " + $data.codeclolor + ";border: 2rpx solid" + $data.codeclolor)
      };
    })
  });
}
const Component = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "C:/Users/86198/Desktop/小程序/SginInSystem/components/handSign/handSign.vue"]]);
wx.createComponent(Component);
