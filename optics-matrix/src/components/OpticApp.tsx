import { OpticCanvas } from "./OpticCanvas";
import { OpticTools } from "./OpticTools";

export function OpticApp() {
  return (
    <div
      style={{
        width: "980px",
        height: "400px",
        background: "grey",
      }}
    >
      <OpticTools
        style={{
          background: "blue",
        }}
        onElementConfig={() => void console.log("config")}
        onElementRemove={() => void console.log("remove")}
        onLensAdd={() => void console.log("add")}
      />
      <OpticCanvas style={{
        height: '100px',
        width: '100%',
      }}
      lens={[{position: 0.5, id: 'hi'}]}
      />
    </div>
  );
}
