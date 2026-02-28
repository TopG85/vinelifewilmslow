/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./assets/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary-green': '#4E7F3A',
        'green-hover': '#3F6B2F',
        'gold-accent': '#D5A33C',
        'warm-white': '#FCFAF5',
        'sage-background': '#E0ECDC',
        'beige-section': '#FAF2E5',
        'main-text': '#2F2F2F',
        'deep-purple': '#4B2E83',
        'deep-forest-green': '#1E6B3A',
        'gold': '#F2C94C',
        'white': '#FFFFFF',
        'soft-grey': '#E5E5E5',
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
