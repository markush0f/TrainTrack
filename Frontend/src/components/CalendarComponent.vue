<template>
    <div>
        <v-calendar ref="calendar" @dayclick="openDialog" />

        <v-dialog v-model="dialogVisible" max-width="500px">
            <v-card>
                <v-card-title>Agregar evento</v-card-title>
                <v-card-text>
                    <v-text-field v-model="eventTitle" label="Título del evento"></v-text-field>
                    <v-text-field v-model="eventDate" label="Fecha del evento" type="date"></v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" @click="saveEvent">Guardar evento</v-btn>
                    <v-btn @click="closeDialog">Cancelar</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { Calendar as VCalendar } from 'v-calendar';

const calendar = ref(null);
const dialogVisible = ref(false);
const eventTitle = ref('');
const eventDate = ref('');

const openDialog = (info) => {
    const selectedDate = info.date;
    eventDate.value = selectedDate.toISOString().split('T')[0]; // Formatea la fecha como "YYYY-MM-DD"
    dialogVisible.value = true;
};

const closeDialog = () => {
    eventTitle.value = '';
    eventDate.value = '';
};

const saveEvent = async () => {
    // Aquí puedes guardar el evento en la base de datos o realizar otras acciones necesarias
    console.log('Evento guardado:', { title: eventTitle.value, date: eventDate.value });
    closeDialog();
};
</script>