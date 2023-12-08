// #ifndef VUE3
import Vue from 'vue'
import App from './App'
import {
	createPinia
} from 'pinia';

Vue.config.productionTip = false
const pinia = createPinia();

App.mpType = 'app'
Vue.use(pinia);

const app = new Vue({
	...App,
	pinia
})
app.$mount()
// #endif

// #ifdef VUE3
import {
	createSSRApp
} from 'vue'
import App from './App.vue'
export function createApp() {
	const app = createSSRApp(App)
	return {
		app
	}
}
// #endif