"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  data() {
    return {
      randomColor: this.generateRandomColor()
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
    // 生成随机颜色的方法
    generateRandomColor() {
      const letters = "6789ABCDEF";
      let color = "#";
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 10)];
      }
      return color;
    },
    // handleCourseClick(courses, course) {
    // 	courses.isFlag = course.classnumber;
    // 	// console.log(courses)
    // 	// 通过$emit将更新后的数据传递到父组件
    // 	this.$emit('course-clicked', this.courses);
    // },
    updateIsFlag(course) {
      this.$emit("updateIsFlag", course.classnumber);
    }
  }
};
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return {
    a: common_vendor.f($props.courses, (course, index, i0) => {
      return {
        a: common_vendor.t(course.classname),
        b: index,
        c: common_vendor.o(($event) => $options.updateIsFlag(course), index)
      };
    }),
    b: $options.generateRandomColor()
  };
}
const Component = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "C:/Users/86198/Desktop/小程序/SginInSystem/components/courseList/courseList.vue"]]);
wx.createComponent(Component);
