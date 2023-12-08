<template>
	<view>
		<uni-icons type="back" size="30" @click="updateIsFlag()"></uni-icons>
		<view class="header">
			<h1>考勤记录</h1>
		</view>
		<h2 class="name">课程号：{{classnumber}}</h2>
		<view class="historyList" v-for="(item,index) in HistoryList" :key="index">
			<view class="Recording">
				<text class="time">{{item.time}}</text>
				<view class="number">
					<text class="already">签到人数：{{item.checkinNumber}}人</text>
					<text class="without">未签到人数：{{item.uncheckinNumber}}人</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name: "showTHistoryList",
		data() {
			return {

			};
		},
		props: {
			HistoryList: {
				type: Object,
			},
			classnumber: {
				type: String,
			},
		},
		methods: {
			updateIsFlag() {
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
	}

	.Recording {
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		font-size: 40rpx;
		margin-top: 30rpx;
		border: 1px solid gray;
	}

	.time {
		font-size: 55rpx
	}

	.already {
		margin-right: 35rpx;
		color: green;
	}

	.without {
		color: red;
	}
</style>