<template>
	<h2 class="choose">请选择你的身份:</h2>
	<view class="Button">
		<button class="teacher">
			<text>我是老师</text>
		</button>
		<button class="student">
			<text>我是学生</text>
		</button>
		<text class="worker">By 北斗小组</text>
	</view>
</template>

<script>
	export default {
		name: "identityChoose",
		data() {
			return {

			};
		}
	}
</script>

<style lang="scss">
	.choose {
		font-size: 1.5em
	}

	.Button {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding-top: 150rpx;
	}

	.teacher {
		font-size: 50rpx;
		font-weight: bold;
		color: white;
		display: flex;
		background-color: seagreen;
		width: 80%;
		height: 300rpx;
		margin-bottom: 200rpx;
		align-items: center;
		justify-content: center;
	}

	.student {
		font-size: 50rpx;
		font-weight: bold;
		color: white;
		display: flex;
		background-color: skyblue;
		width: 80%;
		height: 300rpx;
		align-items: center;
		justify-content: center;
		margin-bottom: 300rpx;
	}

	.worker {
		color: lightgray;
	}
</style>