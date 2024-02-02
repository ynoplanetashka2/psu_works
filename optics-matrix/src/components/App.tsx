import './App.css';
import { OpticCanvas } from "./OpticCanvas";

function App() {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",
        paddingTop: "5rem",
      }}
    >
      <OpticCanvas />
    </div>
  );
}

export default App;
