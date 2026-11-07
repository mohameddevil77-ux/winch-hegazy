/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "D:/winch-hegazy/**/*.html",
    "D:/winch-hegazy/scripts/**/*.py"
  ],
  theme: {
    extend: {
      fontFamily: {
        cairo: ['Cairo', 'sans-serif'],
        tajawal: ['Tajawal', 'sans-serif']
      },
      colors: {
        safety: {
          50: '#fffbeb',
          100: '#fef3c7',
          400: '#fbbf24',
          500: '#f59e0b',
          600: '#d97706'
        },
        rescue: {
          500: '#ef4444',
          600: '#dc2626',
          700: '#b91c1c'
        },
        dark: {
          900: '#0f172a',
          950: '#0b0f17'
        }
      }
    }
  },
  plugins: []
}
