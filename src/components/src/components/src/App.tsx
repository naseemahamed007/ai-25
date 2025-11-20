import TopBar from "./components/TopBar";
import Chat from "./components/Chat";
import Journal from "./components/Journal";

export default function App() {
  return (
    <div className="max-w-5xl mx-auto p-6 space-y-6">
      <TopBar />
      <Chat />
      <Journal />
    </div>
  );
}
