<template>
	<uni-icons type="back" size="30" @click="updateIsFlag()"></uni-icons>
	<view class="code-tip-one">
		<h1>签到码</h1>
	</view>
	<view class="code-test">
		<view class="code-errow" v-if="codeclolor == '#ff0000'">验证码输入错误</view>
		<view class="code-errow" v-else>请完整输入签到码</view>
		<input class="cinput" adjust-position="true" auto-blur="true" @blur="blur" @input="codenum" :focus="focus"
			v-model="code" type="number" maxlength="6" />
	</view>
	<view class="code-input">
		<view v-for="(item,index) in 6" :key="index" @click="codefocus(index)"
			:style='(index == code.length? "border: 5rpx solid #1195db;width: 80rpx;height: 80rpx;line-height: 80rpx;":"color: " + codeclolor + ";" +"border: 2rpx solid" + codeclolor)'>
			{{code[index]}}
		</view>
	</view>
</template>

<script>
	import courseListVue from '../courseList/courseList.vue';
	export default {
		name: "handSign",
		data() {
			return {
				focus: true, //input焦点，用于键盘隐藏后重新唤起
				// 验证码框颜色
				codeclolor: "#313131", //自定义光标的颜色
				code: '', //这是用户输入的验证码
				isWithinTime: false
			};
		},
		props: {
			// 接收来自父组件的课程数据
			courses: {
				type: Object,
				default: () => [],
			},

		},
		methods: {
			updateIsFlag() {
				// 在子组件中通过 $emit 发送事件，将新的 isFlag 传递给父组件
				this.$emit("updateIsFlag", -1); // 这里假设你想将 isFlag 修改为 1
			},
			// 输入验证码
			codenum: function(event) {
				var that = this
				var code = event.target.value
				that.code = code
				if (code.length === 6) {
					const startTime = this.courses.signinTime
					console.log(startTime)
					const currentTime = new Date().getTime()
					console.log(currentTime)
					// 判断是否在签到时间内
					const isWithinTime = currentTime - startTime < (60 * 3 * 1000)
					if (isWithinTime) {
						if (code === this.courses.classCaptcha) {
							//输入六位验证码后自动进行验证并执行验证成功的函数
							uni.showToast({
								title: '签到成功！',
								icon: 'success', //将值设置为 success 或者 ''
								duration: 2000, //持续时间为 2秒
							});
							setTimeout(function() {
								that.updateIsFlag();
							}, 2000);
						} else {
							that.codeclolor = "#ff0000"
							setTimeout(function() {
								that.code = ""
								event.target.value = ""
								that.codeclolor = "#313131"
							}, 1000)
						}
					} else {
						uni.showToast({
							title: '超过签到时间！',
							icon: 'error',
							duration: 2000, //持续时间为 2秒
						});
						setTimeout(function() {
							that.updateIsFlag();
						}, 2000);
					}
				}
			},
			// 键盘隐藏后设置失去焦点
			blur: function() {
				var that = this
				that.focus = false
			},
			// 点击自定义光标显示键盘
			codefocus: function(e) {
				var that = this
				if (e == that.code.length) {
					that.focus = true
				}
			},
		}
	}
</script>

<style lang="scss">
	.code-tip-one {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		text-align: center;
		width: 650rpx;
		height: 250rpx;
		line-height: 100rpx;
		font-size: 60rpx;
		font-weight: bold;
		color: #313131;
	}

	.code-test {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.code-tip {
		width: 650rpx;
		height: 100rpx;
		line-height: 50rpx;
		font-size: 30rpx;
		font-weight: normal;
		color: #8a8a8a;
	}

	.code-errow {
		width: 650rpx;
		height: 50rpx;
		font-size: 28rpx;
		font-weight: normal;
		color: #ff0000;
	}

	.code-tip>text {
		padding: 0 20rpx;
		width: 650rpx;
		font-size: 30rpx;
		font-weight: normal;
		color: #ff5500;
	}

	.code-input {
		margin: auto;
		width: 650rpx;
		height: 100rpx;
		display: flex;
	}

	.code-input>view {
		margin-top: 5rpx;
		margin-left: 15rpx;
		width: 86rpx;
		height: 86rpx;
		line-height: 86rpx;
		font-size: 60rpx;
		font-weight: bold;
		color: #313131;
		text-align: center;
		border-radius: 10rpx;
	}

	.code-input>view:nth-child(1) {
		margin-left: 0rpx;
	}

	.cinput {
		position: fixed;
		left: -100rpx;
		width: 50rpx;
		height: 50rpx;
	}
</style>