import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import { useTokenUserStore } from '@/stores/JWT'
import axios from 'axios'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        requireAuthUser: false
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView,
      meta: {
        requireAuthUser: false,
        // requireAuthTeam: true,
      }
    },
    {
      path: '/Login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
      meta: {
        requireAuthUser: false,
        // requireAuthTeam: true,
      }
    },
    {
      path: '/checkcodeteam',
      name: 'checkcodeteam',
      component: () => import('../views/checkCodeTeamComponent.vue'),
      meta: {
        requireAuthUser: false
      }
    },
    {
      path: '/trainer',
      name: 'trainer',
      component: () => import('../views/TrainerView.vue'),
      meta: {
        // requireAuthUser: true,

      }
    },
    {
      path: '/parent',
      name: 'parent',
      component: () => import('../views/ParentView.vue'),
      meta: {
        // requireAuthUser: true,

      }
    }

  ]
})
// Antes de acceder a cada ruta:
// to: hacia donde, from: de donde viene, next: hacia donde
router.beforeEach(async (to, from, next) => {
  const jwt = {
    'JWT': useTokenUserStore.getToken
  }
  if (to.meta.requireAuthUser) {
    try {
      const res = await axios.get('/api/verify-token')
      console.log("Data:", res.data);
    } catch (e) {
      console.log("Error al verificar el token");
    }
    next('/checkcodeteam')
  } else {
    // Indicamos que puede acceder a esa ruta
    next()
  }
})

export default router
