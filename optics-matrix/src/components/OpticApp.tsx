import { useState } from "react";
import { OpticCanvas } from "./OpticCanvas";
import { OpticTools } from "./OpticTools";
import { LensInfo } from "../optics-matrix-model/LensInfo";

export function OpticApp() {
  const [lenses, setLenses] = useState<ReadonlyArray<LensInfo>>([]);
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
      <OpticCanvas
        style={{
          height: "100px",
          width: "100%",
        }}
        lens={lenses}
      />
    </div>
  );
}
