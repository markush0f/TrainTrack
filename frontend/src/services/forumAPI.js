import axios from "axios";
import { useCookies } from "vue3-cookies";
const { cookies } = useCookies();
const URL = "http://127.0.0.1:8000/api/";
import { useForumStore } from "@/stores/forum";

export async function sendMessageForum(data) {
  const token = cookies.get("token");
  const forumStore = useForumStore();

  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.post(`${URL}forum/sendmessage`, data, {
        headers,
      });
      console.log(res);
      if (res.data.success) {
        console.log("Nuevo mensaje foro:", res.data);
        await loadMessageForum()
      }
    } catch (e) {
      console.log("Error:", e);
    }
  }
}

export async function loadMessageForum() {
  const token = cookies.get("token");
  const forumStore = useForumStore();

  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.get(`${URL}forum/loadmessages`, {
        headers,
      });

      if (res.data.success) {
        console.log("Mensajes foro:", res.data.messages);
        forumStore.messagesForum  = await res.data.messages
      }
    } catch (e) {
      console.log("Error:", e);
    }
  }
}
