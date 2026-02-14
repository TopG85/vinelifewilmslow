/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./assets/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Deep Purple Grapes
        'grape-deep-purple': '#320322',
        'grape-royal-purple': '#4a0e4e',
        'grape-rich-plum': '#6b1e5f',
        
        // Red/Pink Grapes
        'grape-burgundy': '#722f37',
        'grape-wine-red': '#8b2635',
        'grape-rosé': '#c7526b',
        'grape-blush': '#e8a4b8',
        
        // Green Grapes
        'grape-deep-forest': '#2d4a22',
        'grape-midnight-green': '#1a3d1a',
        'grape-emerald': '#4a6741',
        'grape-forest': '#6b8e5a',
        'grape-sage': '#9caf88',
        'grape-chartreuse': '#b8d67c',
        'grape-lime': '#d4e69b',
        'grape-mint': '#e8f5d0',
        'grape-seafoam': '#b8e6b8',
        'grape-olive': '#8fbc8f',
        'grape-spring': '#a8d8a8',
        'grape-hunter': '#355e3b',
        'grape-jade': '#5a7c65',
        'grape-pine': '#1b4332',
        'grape-moss': '#2d5016',
        'grape-fern': '#4f6741',
        'grape-basil': '#7d8471',
        'grape-eucalyptus': '#95a99c',
        'grape-cedar': '#3a5e39',
        'grape-ivy': '#2f4f2f',
        'grape-malachite': '#3f704d',
        'grape-viridian': '#4a6849',
        'grape-laurel': '#6b8a47',
        'grape-thyme': '#8faa54',
        
        // Golden/Yellow Grapes
        'grape-champagne': '#f7e7b4',
        'grape-golden': '#f0d882',
        'grape-amber': '#e6c547',
        
        // Complementary Orange/Coral Palette
        'complement-coral': '#ff6b47',
        'complement-salmon': '#ff8366',
        'complement-peach': '#ffab91',
        // Additional supporting colors
        'cream': '#faf7f0',
        'charcoal': '#2e2e2e',
        'complement-sunset': '#ff7043',
        'complement-terracotta': '#d84315',
        'complement-warm-beige': '#fff3e0',
        'complement-soft-orange': '#ffcc80',
        'vine-brown': '#5d4037',
        'leaf-green': '#689f38',
        'earth-tan': '#8d6e63',
      },
      fontFamily: {
        'crimson': ['Crimson Text', 'serif'],
        'opensans': ['Open Sans', 'sans-serif'],
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
