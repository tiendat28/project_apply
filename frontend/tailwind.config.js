/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './public/index.html',
    './src/**/*.{vue,ts,jsx,tsx,js}',
  ],
  theme: {
    extend: {
      lineHeight: {
        '12': '3rem',
        '11': '50px'
      }
    },
  },
  plugins: [],
}

