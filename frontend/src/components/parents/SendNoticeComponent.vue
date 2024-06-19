<template>
  <div v-if="calendarStore.getEvent()">
    <h2 class="text-2xl font-bold text-center p-5 text-green-700 transition-all">Confirmar asistencia a {{
    calendarStore.getEvent()[0].title }} ({{ calendarStore.getEvent()[0].dateEvent }} {{
    calendarStore.getEvent()[0].dateTime }})
    </h2>
    <form @submit.prevent="submitFormNotices">
      <div class="p-3">
        <ul
          class="items-center w-full text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg sm:flex p-3">
          <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r ">
            <div class="flex items-center ps-3">
              <label class="flex items-center cursor-pointer">
                <input type="radio" name="notice" value="lateEvent" @change="selectNotice($event)"
                  class="form-radio h-5 w-5 text-green-500">
                <span class="ml-2 text-gray-700">LLEGO TARDE</span>
              </label>
            </div>
          </li>
          <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r ">
            <div class="flex items-center ps-3">
              <label class="flex items-center cursor-pointer">
                <input type="radio" name="notice" value="notAttendEvent" @change="selectNotice($event)"
                  class="form-radio h-5 w-5 text-green-500">
                <span class="ml-2 text-gray-700">NO ASISTO</span>
              </label>
            </div>
          </li>
          <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r ">
            <div class="flex items-center ps-3">
              <label class="flex items-center cursor-pointer">
                <input type="radio" name="notice" value="yesAttendEvent" @change="selectNotice($event)"
                  class="form-radio h-5 w-5 text-green-500">
                <span class="ml-2 text-gray-700">SI ASISTO</span>
              </label>
            </div>
          </li>
        </ul>
      </div>
      <textarea id="message" rows="4"
        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300"
        placeholder="Descripción del motivo" v-model="data.other"></textarea>
      <br>
      <div class="flex justify-center">
        <input type="submit" value="Confirmar"
          class="w-2/6  focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 ">
        <button type="button" @click="cancelNotice"
          class=" w-2/6 focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2">Cancelar</button>
      </div>

    </form>
  </div>
  <div v-else>
    <h1 class="text-2xl font-bold text-center p-4 text-green-700">
      Seleccione un evento!
    </h1>
    <h4 class="text-center">
      Pulse en el calendario o en uno de los proximos <br>
      eventos para confirmar o denegar su asistencia.
    </h4>
  </div>
</template>

<script setup>
import { sendNotice } from '@/services/parentsAPI';
import { ref } from 'vue';
import { useCalendarStore } from '@/stores/calendar';
import { useProfileStore } from '@/stores/profile';

const calendarStore = useCalendarStore();
const profile = useProfileStore().data;
const notice = ref('')
const data = ref({
  'title': '',
  'notice': '',
  'other': ''
});

function cancelNotice() {
  calendarStore.cancelEvent();
  console.log(calendarStore.getEvent());
}
function selectNotice(event) {
  notice.value = event.target.value;
  console.log(data.value.other);
  console.log(notice.value);
  console.log(profile.childrens);
};

function submitFormNotices() {
  console.log(data);
  switch (notice.value) {
    case 'lateEvent':
      data.value.notice =
        `${profile.childrens.name} ${profile.childrens.surname} acudirá tarde a 
        ${calendarStore.getEvent()[0].title} el ${calendarStore.getEvent()[0].dateEvent} (${calendarStore.getEvent()[0].dateTime})`;
      data.value.title = calendarStore.getEvent()[0].title;
      break;

    case 'notAttendEvent':
      data.value.notice =
        `${profile.childrens.name} ${profile.childrens.surname} no acudirá a 
        ${calendarStore.getEvent()[0].title} el ${calendarStore.getEvent()[0].dateEvent} (${calendarStore.getEvent()[0].dateTime})`;
      data.value.title = calendarStore.getEvent()[0].title;
      break;

    case 'yesAttendEvent':
      data.value.notice =
        `${profile.childrens.name} ${profile.childrens.surname} acudirá a 
        ${calendarStore.getEvent()[0].title} el ${calendarStore.getEvent()[0].dateEvent} (${calendarStore.getEvent()[0].dateTime})`;
      data.value.title = calendarStore.getEvent()[0].title;
      break;

    default:
      break;
  }
  sendNotice(data.value)
}
</script>