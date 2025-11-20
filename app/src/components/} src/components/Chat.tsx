import { useState } from "react";
import { motion } from "framer-motion";
import { analyze, mood, journal } from "../lib/api";

type Msg = { role: "user" | "ai"; text: string; emotion?: string };

export default function Chat() {
  const [messages, setMessages] = useState<Msg[]>([]);
  const [input, setInput] = useState("");

  async function send() {
    const text = input.trim();
    if (!text) return;
    setInput("");
    setMessages(m => [...m, { role: "user", text }]);
    const res = await analyze(text);
    setMessages(m => [...m, { role: "ai", text: res.reply, emotion: res.emotion }]);
    // Track mood snapshot optimistically
    const now = new Date().getHours();
    const slot = now < 12 ? "morning" : now < 18 ? "afternoon" : "night";
    mood(slot as any, res.emotion);
    // Auto journal on deeper messages
    if (text.length > 50) journal(text);
  }

  return (
    <div className="glass p-6 space-y-4">
      <div className="h-[50vh] overflow-y-auto space-y-3 pr-2">
        {messages.map((m, i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            className={`max-w-[80%] ${m.role === "user" ? "ml-auto" : ""}`}
          >
            <div className={`p-3 rounded-xl ${m.role==="user" ? "bg-white/10" : "bg-neon/10 border border-neon/30"}`}>
              <p className={m.role === "ai" ? "neon-text" : ""}>{m.text}</p>
              {m.emotion && <div className="text-xs text-neon mt-1">Detected: {m.emotion}</div>}
            </div>
          </motion.div>
        ))}
      </div>
      <div className="flex gap-3">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Tell me how you’re feeling..."
          className="flex-1 px-4 py-3 rounded-xl bg-white/5 border border-white/10 focus:outline-none focus:border-neon/60"
        />
        <button onClick={send} className="px-5 py-3 rounded-xl bg-neon text-ink font-medium hover:opacity-90">
          Send
        </button>
      </div>
      <p className="text-xs text-white/50">This AI offers general support, not medical advice.</p>
    </div>
  );
}

