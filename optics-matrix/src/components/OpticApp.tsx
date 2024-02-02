import { OpticCanvas } from "./OpticCanvas";
import { OpticTools } from "./OpticTools";
import { useOpticApp } from "../hooks/useOpticApp";

export function OpticApp() {
  const {
    handleLensClick,
    lensInConfig,
    handleMainOpticLineClick,
    lenses,
    setAppState,
    appState,
    beamVector
  } = useOpticApp();
  return (
    <div
      style={{
        width: "980px",
        height: "400px",
        background: "grey",
      }}
    >
      state: {appState} <br />
      lensInConfig: {lensInConfig}
      <OpticTools
        style={{
          background: "blue",
        }}
        onLensAdd={() => setAppState("addLens")}
        onElementConfig={() => setAppState("configLens")}
        onElementRemove={() => setAppState("removeLens")}
      />
      <OpticCanvas
        style={{
          height: "100px",
          width: "100%",
        }}
        lenses={lenses}
        beamVector={beamVector}
        onLensClick={(lensId: string) => handleLensClick(lensId)}
        onLineClick={(position: number) => handleMainOpticLineClick(position)}
      />
    </div>
  );
}
