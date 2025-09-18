/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        islamic: {
          green: '#0D4F3C',
          gold: '#D4AF37',
          cream: '#F7F3E9'
        }
      }
    },
  },
  plugins: [],
}
