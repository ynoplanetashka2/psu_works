import { nanoid } from "nanoid";
import { useState } from "react";
import { LensInfo } from "../optics-matrix-model/LensInfo";

type OpticAppState = "addLens" | "removeLens" | "configLens";

const DEFAULT_STATE: OpticAppState = "addLens";
export function useOpticApp() {
  const [appState, setAppState] = useState<OpticAppState>(DEFAULT_STATE);
  const [lenses, setLenses] = useState<ReadonlyArray<LensInfo>>([]);
  const [lensInConfig, setLensInConfig] = useState<string | null>(null);

  const handleMainOpticLineClick = (position: number) => {
    switch (appState) {
      case "addLens":
        setLenses((lenses) => [...lenses, { position, id: nanoid() }]);
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

  return {
    handleLensClick,
    handleMainOpticLineClick,
    lenses,
    appState,
    setAppState,
    lensInConfig,
  };
}
