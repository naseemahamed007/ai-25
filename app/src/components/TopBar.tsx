import { motion } from "framer-motion";

export default function TopBar() {
  return (
    <motion.header
      initial={{ y: -20, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      className="glass px-6 py-4 flex items-center justify-between"
    >
      <div className="flex items-center gap-3">
        <div className="w-3 h-3 rounded-full bg-neon animate-pulse" />
        <h1 className="font-semibold neon-text">Emotional AI</h1>
      </div>
      <div className="text-white/70 text-sm">Always here • Private • Non‑judgmental</div>
    </motion.header>
  );
}
