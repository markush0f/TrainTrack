/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'main-green': '#35A439', 
        'second-green': '#4DB138',
        'third-green': '#4ECB3B',
        'black': '#000000',
        'white': '#FFFFFF',
      },
    },
  },
  plugins: [],
}

