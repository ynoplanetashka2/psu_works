import { BeamVector } from "../optics-matrix-model/BeamVector";
import { BeamVectorSettings } from "./BeamVectorSettings";
import { LensSettings } from "./LensSettings";

type LensInfo = {
  position: number;
  refractionCoeff: number;
  radiusOfCurvature: number;
};

type Props = {
  style?: React.HTMLAttributes<HTMLDivElement>["style"];
  lensInfo: LensInfo | null;
  onUpdateLensInfo: (_: LensInfo) => void;
  beamVector: BeamVector;
  onUpdateBeamVector: (_: BeamVector) => void;
};

export function OpticsObjectsSettings({
  style = {},
  lensInfo,
  onUpdateLensInfo,
  beamVector,
  onUpdateBeamVector,
}: Props) {
  return (
    <div style={style}>
      <BeamVectorSettings
        beamVector={beamVector}
        onUpdateBeamVector={onUpdateBeamVector}
      />
      {lensInfo && (
        <LensSettings lensInfo={lensInfo} onUpdateLensInfo={onUpdateLensInfo} />
      )}
    </div>
  );
}
