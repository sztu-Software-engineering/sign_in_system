<template>
	<view class="layout">
		<uni-card class="card">
			<!-- 头像部分 -->
			<view class="content-container">
				<view class="info-container">
					<text class="name">毛毛</text>
					<text class="number">202100202041</text>
				</view>
				<view class="avatar-container">
					<image class="avatar" src="/static/my1.png"></image>
				</view>
			</view>
		</uni-card>
		<button class="add" type="primary" style="width: 250px;" @click="openInputDialog">添加课程</button>
		<view v-show="isInputDialogVisible" class="input-dialog">
			<!-- 弹框内容 -->
			<text class="dialogTitle">加入新班级</text>
			<input class="addCourse" v-model="inputValue" placeholder="请输入课程号" />
			<view class="dialogButton">
				<button @click="cancelInputDialog">取消</button>
				<button @click="confirmInputDialog">确认</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name: "personaldetails",
		data() {
			return {
				isInputDialogVisible: false,
				inputValue: '',
			};
		},
		methods: {
			openInputDialog() {
				// 打开弹框
				this.isInputDialogVisible = true;
				console.log(this.isInputDialogVisible)
			},
			confirmInputDialog() {
				const pattern = /^\d{5}$/;
				if (!pattern.test(this.inputValue)) {
					uni.showToast({
						title: '课程号错误！',
						icon: 'error',
						duration: 2000, //持续时间为 2秒
					});
				} else {
					// 关闭弹框
					this.isInputDialogVisible = false;
				}
				// 清空输入框的值
				this.inputValue = '';
			},
			cancelInputDialog() {
				console.log(this.isInputDialogVisible)
				this.isInputDialogVisible = false;
				// 清空输入框的值
				this.inputValue = '';
			}
		},
	}
</script>

<style lang="scss">
	.input-dialog {
		position: fixed;
		top: 45%;
		left: 50%;
		transform: translate(-50%, -50%);
		height: 450rpx;
		width: 600rpx;
		border: 1px solid #ccc;
		background-color: #fff;
		border-radius: 30px;
	}

	.dialogTitle {
		margin: 0rpx 0 0 160rpx;
		font-size: 50rpx;
		font-weight: bold;
	}

	.addCourse {
		margin: 120rpx 30rpx 20rpx 40rpx;
		font-size: 40rpx;
		border-bottom: 1rpx solid #666;
	}

	.dialogButton {
		margin-top: 80rpx;
		display: flex;
	}

	.dialogButton button {
		width: 230rpx;
		color: white;
		background-color: royalblue;
	}


	.card {
		width: 80%;
		margin: 20px auto;
		padding: 15px;
	}

	.content-container {
		display: flex;
		flex-direction: row;
		/* 让子元素在容器中垂直排列 */
	}


	.avatar {
		width: 120px;
		height: 100px;
		border-radius: 50%;
	}

	.info-container {
		display: flex;
		align-items: center;
		flex-direction: column;
	}

	.avatar-container {
		margin-left: 150rpx;
	}

	.name {
		margin-top: 50rpx;
		font-size: 22px;
		font-weight: bold;
	}

	.number {
		margin-top: 20rpx;
		font-size: 16px;
		color: #666;
	}
</style>