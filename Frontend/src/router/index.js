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
        requireAuthUser: false,
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
    },
    {
      path: '/insertchildrens',
      name: 'insert_childrens',
      component: () => import('')
    }

  ]
})

const { cookies } = useCookies();
const token = cookies.get('token');

router.beforeEach(async (to, from, next) => {

  // if (!token) {
  //   next('/');
  //   console.log("K");
  //   return;
  // }

  console.log("Token:", token != null);

  if (to.meta.requireAuthUser && token) {
    const headers = {
      'Authorization': `Bearer ${token}`
    };

    try {
      const res = await axios.post('/api/authenticatejwt', null, { headers });
      console.log("Response Data:", res.data);
      if (res.data.valid) {
        console.log("Rol:", res.data.rol);
        if (res.data.rol === 'parent' && to.meta.rol === 'parent') {
          console.log("Es un padre");
          next();
          return;
        }
        if (res.data.rol === 'trainer' && to.meta.rol === 'trainer') {
          console.log("Es un entrenador");
          next();
          return;
        }
      }
      next('/notfound');
      return;
    } catch (error) {
      console.log("Error al verificar el token:", error);
      next('/notfound');
      // return;
    }
  } else {
    next();
    return;
  }
});

export default router
