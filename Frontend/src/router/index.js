import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import { useTokenUserStore } from '@/stores/JWT'
import axios from 'axios'
import { useCookies } from 'vue3-cookies'

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
        requireAuthUser: true,
        rol: "trainer"
      }
    },
    {
      path: '/parent',
      name: 'parent',
      component: () => import('../views/ParentView.vue'),
      meta: {
        requireAuthUser: true,
        rol: "parent"

      }
    },
    {
      path: '/trainer/perfil',
      name: 'trainer_perfil',
      component: () => import('../components/ProfileComponent.vue'),
    },
    {
      path: '/notfound',
      name: 'notfound',
      component: () => import('@/views/NotFoundView.vue')
    }

  ]
})

const { cookies } = useCookies();
const token = cookies.get('token')
// import { useRolStore } from '@/stores/ROL';
// const store = useRolStore()
router.beforeEach(async (to, from, next) => {
  const headers = {
    'Authorization': `Bearer ${(token)}`
  }
  // const body = {
  //   'rol': store.rol
  // }
  if (to.meta.requireAuthUser) {
    if (!token) {
      next('/notfound')
      return;
    }
    try {
      const res = await axios.get('/api/authenticatejwt', { headers })
      console.log(token);
      console.log("Data:", res.data);
      if (res.data.valid) next()
      else next('/notfound')
    } catch (e) {
      console.log("Error al verificar el token");
    }
    next('/notfound')
  } else {
    next()
  }
})

export default router
