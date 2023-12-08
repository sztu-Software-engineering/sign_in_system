<template>
	<view>
		<courseList :courses="courselist" v-if="isFlag===-1" @updateIsFlag="updateIsFlag">
		</courseList>
		<!-- 学生签到端 -->
		<handSign :courses="courseData" v-else @updateIsFlag="updateIsFlag"></handSign>
		<!-- 教师发布端 -->
		<!-- <showSign :courses="courseData" :checkInNumber="checkInNumber" v-else @updateIsFlag="updateIsFlag"></showSign> -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				courselist: [{
						classname: '软件工程',
						classnumber: '10001',
					},
					{
						classname: '操作系统',
						classnumber: '10002',
					},
					{
						classname: '计算机网络',
						classnumber: '10003',
					},
				],
				isFlag: -1,
				courseData: {
					classname: '软件工程',
					classnumber: '10001',
					classCaptcha: '143532',
					signinTime: 1600537326048,
				},
				checkInNumber: {
					checkinNumber: 40,
					uncheckinNumber: 20,
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
				// 接收子组件传递的数据并更新父组件中的 isFlag
				this.isFlag = newIsFlag;
				// console.log(this.isFlag)
			},


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

		},
	}
</script>

<style lang="scss">

</style>