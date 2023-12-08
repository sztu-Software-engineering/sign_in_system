<template>
	<view class="layout">
		<view class="login-form" v-if="page===true">
			<h2 class="title">登录页面</h2>
			<view class="username">
				<uni-icons type="contact" size="40"></uni-icons>
				<input class="input" v-model="username" type="text" placeholder="请输入姓名" @blur="usernameRules" />
			</view>
			<view class="usernumber">
				<uni-icons type="wallet" size="40"></uni-icons>
				<input class="input" v-model="usernumber" type="text" placeholder="请输入学号" @blur="usernumberRules" />
			</view>
			<view class="password">
				<uni-icons type="locked" size="40"></uni-icons>
				<input class="input" v-model="password" type="password" placeholder="请包括数字和字母且不低于6位" />
			</view>
			<button class="button" @click="login" size="mini">
				<text class="submit">登录</text>
			</button>
			<text class="goEnroll" @click="changePage">注册账号</text>
		</view>
		<view class="enroll-form" v-else>
			<h2 class="title">注册页面</h2>
			<view class="username">
				<uni-icons type="contact" size="40"></uni-icons>
				<input class="input" v-model="username" type="text" placeholder="请输入姓名" @blur="usernameRules" />
			</view>
			<view class="usernumber">
				<uni-icons type="wallet" size="40"></uni-icons>
				<input class="input" v-model="usernumber" type="text" placeholder="请输入学号" @blur="usernumberRules" />
			</view>
			<view class="password">
				<uni-icons type="locked" size="40"></uni-icons>
				<input class="input" :password="true" v-model="password" type="password" placeholder="请包括数字和字母且不低于6位" />
			</view>
			<view class="repassword">
				<uni-icons type="locked-filled" size="40"></uni-icons>
				<input class="input" v-model="repassword" type="password" placeholder="请再次输入密码" />
			</view>
			<button class="button" @click="enroll" size="mini">
				<text class="submit">注册</text>
			</button>
			<text class="goEnroll" @click="changePage">返回登录</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				usernumber: '',
				username: '',
				password: '',
				repassword: '',
				page: true,
			};
		},
		methods: {
			login() {
				// 在这里添加处理登录逻辑的代码
				// 例如，可以向服务器发送登录请求，验证用户身份等

				// 这里简单地打印用户名和密码，实际应用中需要替换为真实的登录逻辑
				console.log('用户名:', this.username);
				console.log('密码:', this.password);

				// 登录成功后可以跳转到其他页面
				// uni.navigateTo({ url: '/pages/home/index' });
			},
			enroll() {

			},
			usernameRules() {
				const chineseRegex = /^[\u4e00-\u9fa5]+$/;
				// 检查用户名长度是否在2到8之间
				if (!(chineseRegex.test(this.username) && this.username.length >= 2 && this.username.length <= 8)) {
					uni.showToast({
						title: '姓名输入有误！',
						icon: 'error',
						duration: 2000, //持续时间为 2秒
					});
				}
				return chineseRegex.test(this.username) && this.username.length >= 2 && this.username.length <= 8;
			},
			usernumberRules() {
				const regex = /^202\d{9}$/;
				if (!regex.test(this.username)) {
					uni.showToast({
						title: '学号不符合规范！',
						icon: 'error',
						duration: 2000, //持续时间为 2秒
					});
				}
				return regex.test(this.username)
			},
			passwordRules() {
				const passwordRegex = /^(?=.*\d)(?=.*[a-zA-Z]).{7,}$/;
				if (!passwordRegex.test(this.password)) {
					uni.showToast({
						title: '密码不符合规范！',
						icon: 'error',
						duration: 2000, //持续时间为 2秒
					});
				}
				return passwordRegex.test(this.password)
			},
			changePage() {
				this.page = !this.page;
			}
		},
	};
</script>

<style>
	.layout {
		display: flex;
		align-items: center;
		height: 100vh;
		flex-direction: column;
	}

	.login-form {
		display: flex;
		align-items: center;
		flex-direction: column;
		border-radius: 40rpx;
		margin-top: 20vh;
		width: 80%;
		max-width: 400px;
		border: 1rpx solid #000;
		padding: 20rpx 20rpx 40rpx 20rpx;
	}

	.enroll-form {
		display: flex;
		align-items: center;
		flex-direction: column;
		border-radius: 40rpx;
		margin-top: 16vh;
		width: 80%;
		max-width: 400px;
		border: 1rpx solid #000;
		padding: 20rpx 20rpx 40rpx 20rpx;
	}

	.title {
		font-size: 60rpx;
	}

	.username {
		margin-top: 35rpx;
		height: 100rpx;
		display: flex;
	}

	.usernumber {
		margin-top: 35rpx;
		height: 100rpx;
		display: flex;
	}

	.password {
		margin-top: 20rpx;
		height: 100rpx;
		display: flex;
	}

	.repassword {
		margin-top: 20rpx;
		height: 100rpx;
		display: flex;
	}

	.login-form input {
		padding-top: 20rpx;
		margin-left: 20rpx;
		width: 32vh;
	}

	.enroll-form input {
		padding-top: 20rpx;
		margin-left: 20rpx;
		width: 32vh;
	}

	.button {
		width: 80%;
		height: 100rpx;
		background-color: #007aff;
		color: #fff;
		margin-top: 40rpx;
	}

	.submit {
		font-size: 40rpx
	}

	.goEnroll {
		font-size: 25rpx;
		color: darkgreen;
		margin-top: 15rpx;
	}

	.input {
		border-bottom: 1px solid #000;
	}
</style>