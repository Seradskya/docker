import {createRouter, createWebHistory} from 'vue-router'
import MyDashboard from '@/views/DashboardView.vue';
import MyNote from '@/views/NoteView.vue';
import EditNoteView from '@/views/EditNoteView.vue';
import store from '@/store'; // NEW


const routes = [
  {
    path: '/',
    name: 'MyDashboard',
    component: MyDashboard,
  },
  {
    path: '/note/:id',
    name: 'MyNote',
    component: MyNote,
    props: true,
  },
  {
    path: '/editnote/:id',
    name: 'EditNote',
    component: EditNoteView,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;
