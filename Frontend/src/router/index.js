import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignupView from "../views/SignupView.vue";
import axios from "axios";
import { useCookies } from "vue3-cookies";
import InsertPlayerComponent from "@/components/players/InsertPlayerComponent.vue";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
      meta: {
        requireAccountUser: false,
        // requireAuthTeam: true,
      },
    },
    {
      path: "/Login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
      meta: {
        // requireAccountUser: true,
        requireVerifyUser: true,
      },
    },
    {
      path: "/checkcodeteam",
      name: "checkcodeteam",
      component: () => import("../views/teams/checkCodeTeamComponent.vue"),
      meta: {
        requireAuthUser: true,
      },
    },
    {
      path: "/trainer",
      name: "trainer",
      component: () => import("../views/trainers/TrainerView.vue"),
      meta: {
        requireAuthUser: true,
        rol: "trainer",
      },
    },
    {
      path: "/parent",
      name: "parent",
      component: () => import("../views/parents/ParentView.vue"),
      meta: {
        requireAuthUser: true,
        rol: "parent",
      },
    },
    {
      path: "/trainer/perfil",
      name: "trainer_perfil",
      component: () => import("../components/ProfileComponent.vue"),
    },
    {
      path: "/notfound",
      name: "notfound",
      component: () => import("@/views/NotFoundView.vue"),
    },
    {
      path: "/trainer/insertplayer",
      name: "insert_childrens",
      component: InsertPlayerComponent,
    },
    {
      path: "/forum",
      name: "forum",
      component: () => import("@/views/forum/ForumView.vue")
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import("@/views/ContactView.vue")
    },
    {
      path: '/aboutus',
      name: 'aboutus',
      component: () => import("@/views/AboutUs.vue")
    }
  ],
});

const { cookies } = useCookies();
router.beforeEach(async (to, from, next) => {
  const token = cookies.get("token");

  if (to.meta.requireAuthUser) {
    const headers = {
      Authorization: `Bearer ${token}`,
    };
    try {
      const res = await axios.post("/api/authenticatejwt", null, { headers });
      console.log("Response Data:", res.data);
      if (res.data.valid) {
        // console.log("Rol:", res.data.rol);
        if (res.data.rol === "parent" && to.meta.rol === "parent") {
          next();
          return;
        }
        if (res.data.rol === "trainer" && to.meta.rol === "trainer") {
          // console.log("Es un entrenador");
          next();
          return;
        }
      }
      next("/login");
      return;
    } catch (error) {
      console.log("Error al verificar el token:", error);
      next("/login");
      return;
    }
  } else {
    next();
    return;
  }
});

export default router;
