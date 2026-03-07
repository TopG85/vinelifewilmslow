/** @type {import('tailwindcss').Config} */
const fontStacks = {
  ui: ['SohneSchmal', 'Sohne Schmal', 'Inter', 'sans-serif'],
  display: ['SohneSchmal', 'Sohne Schmal', 'Inter', 'sans-serif'],
  alt: ['SohneSchmal', 'Sohne Schmal', 'Inter', 'sans-serif'],
};

module.exports = {
  content: [
    "./index.html",
    "./assets/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Deep Green
        'Deep-Green': '#2F6E4F',
        // Light Green
        'Light-Green': '#78B77A',
        // White
        'White': '#FFFFFF',
        // Orange
        'Orange': '#C96A3A',
        // Gray
        'Gray': '#6E776F'

      },
      fontFamily: {
        sans: fontStacks.ui,
        ui: fontStacks.ui,
        display: fontStacks.display,
        alt: fontStacks.alt,

        // Backward-compatible aliases for existing utility usage.
        lato: fontStacks.ui,
        montserrat: fontStacks.display,
        playfair: fontStacks.alt,
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
