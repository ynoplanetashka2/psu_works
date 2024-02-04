import { nanoid } from "nanoid";
import { useState } from "react";
import { LensInfo } from "../types/LensInfo";
import { BeamVector } from "../optics-matrix-model/BeamVector";

export type OpticAppState = "addLens" | "removeLens" | "configLens";

const DEFAULT_STATE: OpticAppState = "addLens";
const DEFAULT_BEAM_VECTOR: BeamVector = [0, 0];
export function useOpticApp() {
  const [appState, setAppState] = useState<OpticAppState>(DEFAULT_STATE);
  const [lenses, setLenses] = useState<ReadonlyArray<LensInfo>>([]);
  const [lensInConfig, setLensInConfig] = useState<string | null>(null);
  const [beamVector, setBeamVector] = useState<BeamVector>(DEFAULT_BEAM_VECTOR);

  const handleMainOpticLineClick = (position: number) => {
    switch (appState) {
      case "addLens":
        setLenses((lenses) => [
          ...lenses,
          { position, refractionCoeff: 1, radiusOfCurvature: 1, id: nanoid() },
        ]);
        break;
      case "configLens":
      case "removeLens":
        break;
    }
  };
  const handleLensClick = (lensId: string) => {
    switch (appState) {
      case "addLens":
        break;
      case "configLens":
        setLensInConfig(lensId);
        break;
      case "removeLens":
        if (lensInConfig === lensId) {
          setLensInConfig(null);
        }
        setLenses((lenses) => lenses.filter(({ id }) => id !== lensId));
    }
  };
  function updateLensInConfig(lensInfo: LensInfo) {
    const lensInConfigIndex = lenses.findIndex(({ id }) => id === lensInConfig);
    setLenses((lenses) =>
      lenses.map((lens, index) => {
        if (index !== lensInConfigIndex) {
          return lens;
        }
        return lensInfo;
      })
    );
  }

  return {
    handleLensClick,
    handleMainOpticLineClick,
    lenses,
    appState,
    setAppState,
    lensInConfig: lenses.find(({ id }) => id === lensInConfig) ?? null,
    updateLensInConfig: updateLensInConfig,
    beamVector,
    setBeamVector,
  };
}
