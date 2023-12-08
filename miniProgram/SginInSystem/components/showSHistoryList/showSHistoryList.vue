<template>
	<view>
		<uni-icons type="back" size="30" @click="updateIsFlag()"></uni-icons>
		<view class="header">
			<h1>签到记录</h1>
		</view>
		<h2 class="name">{{classname}}</h2>
		<view class="historyList" v-for="(item,index) in HistoryList" :key="index">
			<view class="Recording">
				<text class="time">{{item.time}}</text>
				<text v-if="item.state===1">签到成功</text>
				<text v-else>签到失败</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name: "showHistoryList",
		data() {
			return {

			};
		},
		props: {
			HistoryList: {
				type: Object,
			},
			classname: {
				type: String,
			},
		},
		methods: {
			updateIsFlag() {
				// console.log(course.classnumber)
				// 在子组件中通过 $emit 发送事件，将新的 isFlag 传递给父组件
				this.$emit("updateIsFlag", -1); // 这里假设你想将 isFlag 修改为 1
			},
		},
	}
</script>

<style lang="scss">
	.header {
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 60rpx;
		font-weight: bold;
	}

	.name {
		font-size: 50rpx;
		margin: 20rpx;
		color: brown;
	}

	.historyList {
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		border-bottom: 1px solid gray;
	}

	.Recording {
		font-size: 40rpx;
		margin-top: 30rpx;
	}

	.time {
		margin-right: 25rpx;
	}
</style>