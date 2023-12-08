"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  data() {
    return {
      courselist: [
        {
          classname: "软件工程",
          classnumber: "10001"
        },
        {
          classname: "操作系统",
          classnumber: "10002"
        },
        {
          classname: "计算机网络",
          classnumber: "10003"
        }
      ],
      isFlag: -1,
      courseData: {
        classname: "软件工程",
        classnumber: "10001",
        classCaptcha: "143532",
        signinTime: 1600537326048
      },
      checkInNumber: {
        checkinNumber: 40,
        uncheckinNumber: 20
      }
    };
  },
  // mounted() {
  // 	// 发送 HTTP 请求获取后端的对象数组数据
  // 	this.fetchObjectArray();
  // },
  methods: {
    // 处理子组件传递过来的点击事件
    updateIsFlag(newIsFlag) {
      this.isFlag = newIsFlag;
    }
    // fetchObjectArray() {
    // 	// 假设发送 GET 请求获取对象数组数据的 URL 是 '/api/getObjectArray'
    // 	uni.request({
    // 		url: '/api/getObjectArray',
    // 		method: 'GET',
    // 		success: (res) => {
    // 			// 在请求成功后，处理返回的数据
    // 			if (res.statusCode === 200) {
    // 				// 假设后端返回的数据在 res.data 中是一个对象数组
    // 				this.courselist = res.data;
    // 			}
    // 		},
    // 		fail: (err) => {
    // 			console.error('请求失败', err);
    // 		},
    // 	});
    // },
  }
};
if (!Array) {
  const _easycom_courseList2 = common_vendor.resolveComponent("courseList");
  const _easycom_handSign2 = common_vendor.resolveComponent("handSign");
  (_easycom_courseList2 + _easycom_handSign2)();
}
const _easycom_courseList = () => "../../components/courseList/courseList.js";
const _easycom_handSign = () => "../../components/handSign/handSign.js";
if (!Math) {
  (_easycom_courseList + _easycom_handSign)();
}
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return common_vendor.e({
    a: $data.isFlag === -1
  }, $data.isFlag === -1 ? {
    b: common_vendor.o($options.updateIsFlag),
    c: common_vendor.p({
      courses: $data.courselist
    })
  } : {
    d: common_vendor.o($options.updateIsFlag),
    e: common_vendor.p({
      courses: $data.courseData
    })
  });
}
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "C:/Users/86198/Desktop/小程序/SginInSystem/pages/sign/sign.vue"]]);
wx.createPage(MiniProgramPage);
