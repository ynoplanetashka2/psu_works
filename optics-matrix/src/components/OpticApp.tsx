import { OpticCanvas } from "./OpticCanvas";
import { OpticTools } from "./OpticTools";
import { useOpticApp } from "../hooks/useOpticApp";
import { OpticsObjectsSettings } from "./OpticsObjectsSettings";

export function OpticApp() {
  const {
    handleLensClick,
    lensInConfig,
    handleMainOpticLineClick,
    lenses,
    setAppState,
    appState,
    beamVector,
    setBeamVector,
    updateLensInConfig,
  } = useOpticApp();
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
        onLensAdd={() => setAppState("addLens")}
        onElementConfig={() => setAppState("configLens")}
        onElementRemove={() => setAppState("removeLens")}
      />
      <OpticsObjectsSettings
        lensInfo={lensInConfig}
        onUpdateLensInfo={(lensInfo) => {
          if (lensInConfig === null) {
            return;
          }
          updateLensInConfig({
            ...lensInConfig,
            ...lensInfo,
          });
        }}
        beamVector={beamVector}
        onUpdateBeamVector={(newBeamVector) => setBeamVector(newBeamVector)}
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
