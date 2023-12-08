<template>
	<view>
		<courseList :courses="courselist" v-if="isFlag===-1" @updateIsFlag="updateIsFlag"></courseList>
		<!-- 学生 -->
		<!-- <showSHistoryList :HistoryList="SHistoryList" :classname="classname" v-else @updateIsFlag="updateIsFlag">
		</showSHistoryList> -->
		<!-- 教师 -->
		<showTHistoryList :HistoryList="THistoryList" :classnumber="classnumber" v-else @updateIsFlag="updateIsFlag">
		</showTHistoryList>
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
				SHistoryList: [{
						time: "2023.01.11 16:30:00",
						state: 1 //是否签到成功
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
						state: 1 //是否签到成功
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
				],
				THistoryList: [{
						time: "2023.01.11 16:30:00",
						checkinNumber: 40,
						uncheckinNumber: 20,
					},
					{
						time: "2023.03.21 18:24:00",
						checkinNumber: 40,
						uncheckinNumber: 20,
					},
					{
						time: "2023.10.14 09:45:40",
						checkinNumber: 40,
						uncheckinNumber: 20,
					},
					{
						time: "2023.11.11 09:20:00",
						checkinNumber: 40,
						uncheckinNumber: 20,
					},
					{
						time: "2023.01.11 16:30:00",
						checkinNumber: 40,
						uncheckinNumber: 20,
					},
					{
						time: "2023.03.21 18:24:00",
						checkinNumber: 40,
						uncheckinNumber: 20,
					},
					{
						time: "2023.10.14 09:45:40",
						checkinNumber: 40,
						uncheckinNumber: 20,
					},
					{
						time: "2023.11.11 09:20:00",
						checkinNumber: 40,
						uncheckinNumber: 20,
					},
				],
				isFlag: 1,
				classname: '软件工程',
				classnumber: '10001',
			};
		},
		methods: {
			updateIsFlag(newIsFlag) {
				// 接收子组件传递的数据并更新父组件中的 isFlag
				this.isFlag = newIsFlag;
				// console.log(this.isFlag)
			},
		},
	}
</script>

<style lang="scss">

</style>