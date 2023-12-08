<template>
	<view class="List">
		<h2 class="title">您的课程</h2>
		<view v-for="(course, index) in courses" :key="index" class="courseList"
			:style="{ backgroundColor: generateRandomColor()}" @click="updateIsFlag(course)">
			<!-- 渲染课程信息 -->
			<text class="courseText">{{ course.classname }}</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				randomColor: this.generateRandomColor(),
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
			// 生成随机颜色的方法
			generateRandomColor() {
				const letters = '6789ABCDEF';
				let color = '#';
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
				// console.log(course.classnumber)
				// 在子组件中通过 $emit 发送事件，将新的 isFlag 传递给父组件
				this.$emit("updateIsFlag", course.classnumber); // 这里假设你想将 isFlag 修改为 1
			},
		},
	}
</script>

<style lang="scss">
	.List {
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}

	.courseList {
		height: 100rpx;
		width: 80%;
		margin: 20rpx;
		border: 1px solid #ccc;
		display: flex;
		justify-content: center;
		align-items: center;
		color: white;
	}

	.title {
		font-size: 40rpx;
		margin-bottom: 40rpx;
	}
</style>