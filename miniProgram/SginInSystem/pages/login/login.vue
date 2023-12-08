<template>
	<view>
		<!-- <identityChoose></identityChoose> -->
		<Login></Login>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				Authentication: 0 //身份认证，0为学生，1为老师
			};
		},
		onShow() {
			uni.hideHomeButton()
		}
	}
</script>

<style lang="scss">

</style>