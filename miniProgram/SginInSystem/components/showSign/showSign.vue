<template>
	<uni-icons type="back" size="30" @click="updateIsFlag()"></uni-icons>
	<view class="showCaptcha">
		<h2 class="title">本次的验证码为：</h2>
		<text class="captcha">{{Captcha}}</text>
	</view>
	<view class="text">
		<text class="already">已签到：{{checkInNumber.checkinNumber}}</text>
		<text class="without">未签到：{{checkInNumber.uncheckinNumber}}</text>
	</view>
</template>

<script>
	export default {
		name: "showSign",
		data() {
			return {
				Captcha: '-1'
			};
		},
		props: {
			// 接收来自父组件的课程数据
			courses: {
				type: Object,
				default: () => [],
			},
			checkInNumber: {
				type: Object
			}
		},
		methods: {
			updateIsFlag() {
				// console.log(course.classnumber)
				// 在子组件中通过 $emit 发送事件，将新的 isFlag 传递给父组件
				this.$emit("updateIsFlag", -1); // 这里假设你想将 isFlag 修改为 1
			},
		},
		mounted() {
			this.Captcha = this.courses.classCaptcha
		}
	}
</script>

<style lang="scss">
	.showCaptcha {
		height: 800rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin-bottom: 80rpx;
	}

	.title {
		font-size: 60rpx;
		color: firebrick
	}

	.captcha {
		margin-top: 40rpx;
		font-size: 100rpx;
		color: darkgreen
	}

	.already {
		font-size: 50rpx;
		color: green;
	}

	.without {
		margin-left: 160rpx;
		font-size: 50rpx;
		color: red;
	}
</style>