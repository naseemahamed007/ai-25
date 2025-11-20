import { useState } from "react";
import { journal } from "../lib/api";

export default function Journal() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [insights, setInsights] = useState<string[]>([]);

  async function save() {
    const { summary, insights } = await journal(text);
    setSummary(summary); setInsights(insights);
    setText("");
  }

  return (
    <div className="glass p-6 space-y-4">
      <h3 className="font-semibold">Journaling assistant</h3>
      <textarea
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="Write freely. I’ll highlight insights."
        className="w-full h-32 px-4 py-3 rounded-xl bg-white/5 border border-white/10"
      />
      <button onClick={save} className="px-5 py-3 rounded-xl bg-magenta text-white font-medium">Save & analyze</button>
      {summary && (
        <div className="mt-4">
          <p className="text-white/70 text-sm">Summary</p>
          <p className="neon-text">{summary}</p>
          <p className="text-white/70 text-sm mt-3">Insights</p>
          <ul className="list-disc list-inside">
            {insights.map((i, idx) => <li key={idx}>{i}</li>)}
          </ul>
        </div>
      )}
    </div>
  );
}
