/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'main-green': '#4DB138',
        'second-green': '#35A439',
        // 'third-green': '#4ECB3B',
        'green-navbar': '#006B38FF',
        'black': '#000000',
        'white': '#FFFFFF',
        // Prueba colores
        'dark-green': '#1E7E34',
        'light-gray': '#CCCCCC',
        'third-green': '#2BAE66FF',
        'white-gray': '#FCF6F5FF',
        'navbar-bg': '#F5F5F5'
      },
    },
  },
  plugins: [],
}

