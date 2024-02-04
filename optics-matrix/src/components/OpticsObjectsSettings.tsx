import { BeamVectorSettings } from "./BeamVectorSettings";
import { LensSettings } from "./LensSettings";

type LensInfo = {
  position: number;
  refractionCoeff: number;
};

type Props = {
  style?: React.HTMLAttributes<HTMLDivElement>["style"];
  lensInfo: LensInfo | null;
  onUpdateLensInfo: (_: LensInfo) => void;
};

export function OpticsObjectsSettings({
  style = {},
  lensInfo,
  onUpdateLensInfo,
}: Props) {
  return (
    <div style={style}>
      <BeamVectorSettings />
      {lensInfo && (
        <LensSettings lensInfo={lensInfo} onUpdateLensInfo={onUpdateLensInfo} />
      )}
    </div>
  );
}
