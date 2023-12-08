// store/userStore.js
import {
	defineStore
} from 'pinia';

export const useUserStore = defineStore({
	id: 'user',
	state: () => ({
		userData: null,
	}),
	actions: {
		setUserData(data) {
			this.userData = data;
		},
	},
});