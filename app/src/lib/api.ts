import axios from "axios";
export const api = axios.create({ baseURL: "http://localhost:8000" });

export async function analyze(text: string) {
  const { data } = await api.post("/analyze", { text });
  return data;
}
export async function journal(text: string) {
  const { data } = await api.post("/journal", { text });
  return data;
}
export async function mood(timeOfDay: "morning"|"afternoon"|"night", emotion: string) {
  const { data } = await api.post("/mood", { timeOfDay, emotion });
  return data;
}
