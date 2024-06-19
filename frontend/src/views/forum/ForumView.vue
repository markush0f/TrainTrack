<template>
  <div class="bg-white-100">
    <div class="container mx-auto px-4 py-4">
      <h1
        class="text-4xl font-semibold mb-4 flex justify-center text-green-600"
      >
        Chat de equipo
      </h1>
      <div class="space-y-1 overflow-auto max-h-96">
        <div
          :class="{
            '': index % 2 === 0,
            'bg-gray-100 ': index % 2 !== 0,
          }"
          class="p-3 border-b-2 rounded-l-full"
          v-for="(message, index) in forumStore.messagesForum"
          :key="message.id"
        >
          <div class="flex justify-between">
            <div class="ml-4 text-left">
              <h2 class="text-lg font-semibold mb-1">{{ message.title }}</h2>
            </div>
            <div class="text-right">
              <p class="text-sm text-gray-500">{{ message.author }}</p>
            </div>
          </div>
          <div class="flex justify-between">
            <div class="ml-10 text-left">
              <p class="text-gray-700 mb-2">{{ message.message }}</p>
            </div>
            <div class="text-right">
              <p class="text-sm text-gray-700 mb-2">{{ message.created_at }}</p>
            </div>
          </div>
          <div class="flex items-center justify-between"></div>
        </div>
      </div>
      <div class="mt-8">
        <h2 class="text-lg font-semibold mb-2">Nueva Publicación</h2>
        <form @submit.prevent="submitForm">
          <div class="mb-2">
            <label for="titulo" class="block text-gray-700 font-bold mb-1"
              >Título</label
            >
            <input
              type="text"
              id="titulo"
              name="titulo"
              class="w-full px-3 py-2 rounded-lg border focus:outline-none focus:border-green-500"
              v-model="data.title"
              required
            />
          </div>
          <div class="mb-2">
            <label for="contenido" class="block text-gray-700 font-bold mb-1"
              >Contenido</label
            >
            <textarea
              id="contenido"
              name="contenido"
              rows="4"
              class="w-full px-3 py-2 rounded-lg border focus:outline-none focus:border-green-500"
              v-model="data.message"
              required
            ></textarea>
          </div>
          <div>
            <button
              type="submit"
              class="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700"
            >
              Publicar
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProfileStore } from "@/stores/profile";
import { onMounted } from "vue";
import { loadMessageForum, sendMessageForum } from "@/services/forumAPI";
import { useForumStore } from "@/stores/forum";
const forumStore = useForumStore();

const profile = useProfileStore();
const dataForum = {
  team: profile.data.team,
};
const data = {
  title: "",
  message: "",
};

async function submitForm() {
  console.log(data);
  await sendMessageForum(data);
}

onMounted(async () => {
  await loadMessageForum();
  console.log(forumStore.messagesForum);
});
</script>
