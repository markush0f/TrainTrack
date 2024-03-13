import axios from 'axios';
import { useCookies } from "vue3-cookies";
const URL = "http://127.0.0.1:8000/api/"
const { cookies } = useCookies();

// Solicitud para enviar un mensaje