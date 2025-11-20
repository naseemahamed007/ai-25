import { motion } from "framer-motion";

export default function MoodChart({ weekly }: { weekly?: any }) {
  const slots = ["morning", "afternoon", "night"];
  const emotions = ["happy","sad","angry","stress","excited","lonely","confused","neutral"];
  return (
    <div className="glass p-6">
      <h3 className="mb-4 font-semibold">Weekly mood</h3>
      <div className="grid grid-cols-3 gap-4">
        {slots.map(slot => (
          <div key={slot}>
            <p className="text-white/70 text-sm">{slot}</p>
            <div className="mt-2 space-y-1">
              {emotions.map(e => {
                const v = weekly?.[slot]?.[e] ?? 0;
                return (
                  <motion.div key={e} initial={{ width: 0 }} animate={{ width: `${Math.min(v*12, 100)}%` }} className="h-2 bg-neon/30 rounded" />
                )
              })}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
