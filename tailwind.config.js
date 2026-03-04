/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./assets/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Deep Green
        'Deep-Green': '#2F6237'
        // Deep Purple 
        'Deep-Purple': '#3B1C4A'
        // White
        'White': '#FFFFFF'
        // Gold Yellow
        'Gold-Yellow': '#EFC643'
      },
      fontFamily: {
        'lato': ['Lato', 'Arial', 'sans-serif'],
        'montserrat': ['Montserrat', 'Arial', 'sans-serif'],
        'playfair': ['Playfair Display', 'serif'],
      },
      minHeight: {
        'screen-minus-nav': 'calc(100vh - 90px)',
      },
      transitionDuration: {
        '400': '400ms',
      },
      rotate: {
        '5': '5deg',
      },
    },
  },
  plugins: [],
}
