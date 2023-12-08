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
      SHistoryList: [
        {
          time: "2023.01.11 16:30:00",
          state: 1
          //是否签到成功
        },
        {
          time: "2023.03.21 18:24:00",
          state: 0
        },
        {
          time: "2023.10.14 09:45:40",
          state: 1
        },
        {
          time: "2023.11.11 09:20:00",
          state: 0
        },
        {
          time: "2023.01.11 16:30:00",
          state: 1
          //是否签到成功
        },
        {
          time: "2023.03.21 18:24:00",
          state: 0
        },
        {
          time: "2023.10.14 09:45:40",
          state: 1
        },
        {
          time: "2023.11.11 09:20:00",
          state: 0
        }
      ],
      THistoryList: [
        {
          time: "2023.01.11 16:30:00",
          checkinNumber: 40,
          uncheckinNumber: 20
        },
        {
          time: "2023.03.21 18:24:00",
          checkinNumber: 40,
          uncheckinNumber: 20
        },
        {
          time: "2023.10.14 09:45:40",
          checkinNumber: 40,
          uncheckinNumber: 20
        },
        {
          time: "2023.11.11 09:20:00",
          checkinNumber: 40,
          uncheckinNumber: 20
        },
        {
          time: "2023.01.11 16:30:00",
          checkinNumber: 40,
          uncheckinNumber: 20
        },
        {
          time: "2023.03.21 18:24:00",
          checkinNumber: 40,
          uncheckinNumber: 20
        },
        {
          time: "2023.10.14 09:45:40",
          checkinNumber: 40,
          uncheckinNumber: 20
        },
        {
          time: "2023.11.11 09:20:00",
          checkinNumber: 40,
          uncheckinNumber: 20
        }
      ],
      isFlag: 1,
      classname: "软件工程",
      classnumber: "10001"
    };
  },
  methods: {
    updateIsFlag(newIsFlag) {
      this.isFlag = newIsFlag;
    }
  }
};
if (!Array) {
  const _easycom_courseList2 = common_vendor.resolveComponent("courseList");
  const _easycom_showTHistoryList2 = common_vendor.resolveComponent("showTHistoryList");
  (_easycom_courseList2 + _easycom_showTHistoryList2)();
}
const _easycom_courseList = () => "../../components/courseList/courseList.js";
const _easycom_showTHistoryList = () => "../../components/showTHistoryList/showTHistoryList.js";
if (!Math) {
  (_easycom_courseList + _easycom_showTHistoryList)();
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
      HistoryList: $data.THistoryList,
      classnumber: $data.classnumber
    })
  });
}
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "C:/Users/86198/Desktop/小程序/SginInSystem/pages/signHistory/signHistory.vue"]]);
wx.createPage(MiniProgramPage);
