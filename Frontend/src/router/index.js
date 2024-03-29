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
        requireAccountUser: true,
      },
    },
    {
      path: "/trainer",
      name: "trainer",
      component: () => import("../views/trainers/TrainerView.vue"),
      meta: {
        requireAccountUser: true,
        rol: "trainer",
        // requireVerifyUser: true,
      },
    },
    {
      path: "/parent",
      name: "parent",
      component: () => import("../views/parents/ParentView.vue"),
      meta: {
        requireAccountUser: true,
        requireVerifyUser: true,
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
    {},
  ],
});

const { cookies } = useCookies();
router.beforeEach(async (to, from, next) => {
  const token = cookies.get("token");

  if (to.meta.requireAccountUser) {
    const headers = {
      Authorization: `Bearer ${token}`,
    };
    try {
      const res = await axios.post("/api/checkAccountUser", null, { headers });
      console.log("Response Data:", res.data);
      if (res.data.register) {
        if (
          (res.data.rol === "parent" && to.meta.rol === "parent") ||
          (res.data.rol === "trainer" && to.meta.rol === "trainer") ||
          to.path === "/checkcodeteam"
        ) {
          next();
          return; 
        }
      }
      next("/signup");
      return;
    } catch (error) {
      console.log("Error: ", error);
      next("/signup");
      return;
    }
  }
  // Comprobamos si la verificacion del usuario es valida
  if (to.meta.requireVerifyUser) {
    const headers = {
      Authorization: `Bearer ${token}`,
    };
    try {
      const res = await axios.post("/api/checkCodeTeam", null, { headers });
      console.log(res.data);
      if (res.data.validCodeTeam) {
        next();
        return; 
      } else {
        next("/");
        return; 
      }
    } catch (error) {
      console.log("Error: ", error);
      next("/");
      return; 
    }
  }
  next(); 

  // Comprobamos el rol del usuario para ver a que apartado puede acceder
});
export default router;
