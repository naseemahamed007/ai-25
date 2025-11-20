export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#0b0f17",
        neon: "#7cfcff",
        magenta: "#ff3cac",
        violet: "#8a00ff"
      },
      boxShadow: {
        glow: "0 0 30px rgba(124,252,255,0.4)"
      },
      backdropBlur: {
        xs: "2px"
      }
    }
  },
  plugins: []
};
