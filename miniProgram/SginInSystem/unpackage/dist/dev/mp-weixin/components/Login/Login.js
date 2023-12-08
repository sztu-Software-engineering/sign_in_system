"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  data() {
    return {
      usernumber: "",
      username: "",
      password: "",
      repassword: "",
      page: true
    };
  },
  methods: {
    login() {
      console.log("用户名:", this.username);
      console.log("密码:", this.password);
    },
    enroll() {
    },
    usernameRules() {
      const chineseRegex = /^[\u4e00-\u9fa5]+$/;
      if (!(chineseRegex.test(this.username) && this.username.length >= 2 && this.username.length <= 8)) {
        common_vendor.index.showToast({
          title: "姓名输入有误！",
          icon: "error",
          duration: 2e3
          //持续时间为 2秒
        });
      }
      return chineseRegex.test(this.username) && this.username.length >= 2 && this.username.length <= 8;
    },
    usernumberRules() {
      const regex = /^202\d{9}$/;
      if (!regex.test(this.username)) {
        common_vendor.index.showToast({
          title: "学号不符合规范！",
          icon: "error",
          duration: 2e3
          //持续时间为 2秒
        });
      }
      return regex.test(this.username);
    },
    passwordRules() {
      const passwordRegex = /^(?=.*\d)(?=.*[a-zA-Z]).{7,}$/;
      if (!passwordRegex.test(this.password)) {
        common_vendor.index.showToast({
          title: "密码不符合规范！",
          icon: "error",
          duration: 2e3
          //持续时间为 2秒
        });
      }
      return passwordRegex.test(this.password);
    },
    changePage() {
      this.page = !this.page;
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
    a: $data.page === true
  }, $data.page === true ? {
    b: common_vendor.p({
      type: "contact",
      size: "40"
    }),
    c: common_vendor.o((...args) => $options.usernameRules && $options.usernameRules(...args)),
    d: $data.username,
    e: common_vendor.o(($event) => $data.username = $event.detail.value),
    f: common_vendor.p({
      type: "wallet",
      size: "40"
    }),
    g: common_vendor.o((...args) => $options.usernumberRules && $options.usernumberRules(...args)),
    h: $data.usernumber,
    i: common_vendor.o(($event) => $data.usernumber = $event.detail.value),
    j: common_vendor.p({
      type: "locked",
      size: "40"
    }),
    k: $data.password,
    l: common_vendor.o(($event) => $data.password = $event.detail.value),
    m: common_vendor.o((...args) => $options.login && $options.login(...args)),
    n: common_vendor.o((...args) => $options.changePage && $options.changePage(...args))
  } : {
    o: common_vendor.p({
      type: "contact",
      size: "40"
    }),
    p: common_vendor.o((...args) => $options.usernameRules && $options.usernameRules(...args)),
    q: $data.username,
    r: common_vendor.o(($event) => $data.username = $event.detail.value),
    s: common_vendor.p({
      type: "wallet",
      size: "40"
    }),
    t: common_vendor.o((...args) => $options.usernumberRules && $options.usernumberRules(...args)),
    v: $data.usernumber,
    w: common_vendor.o(($event) => $data.usernumber = $event.detail.value),
    x: common_vendor.p({
      type: "locked",
      size: "40"
    }),
    y: $data.password,
    z: common_vendor.o(($event) => $data.password = $event.detail.value),
    A: common_vendor.p({
      type: "locked-filled",
      size: "40"
    }),
    B: $data.repassword,
    C: common_vendor.o(($event) => $data.repassword = $event.detail.value),
    D: common_vendor.o((...args) => $options.enroll && $options.enroll(...args)),
    E: common_vendor.o((...args) => $options.changePage && $options.changePage(...args))
  });
}
const Component = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "C:/Users/86198/Desktop/小程序/SginInSystem/components/Login/Login.vue"]]);
wx.createComponent(Component);
