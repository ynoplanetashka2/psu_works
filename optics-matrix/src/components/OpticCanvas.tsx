import { BeamVector } from "../optics-matrix-model/BeamVector";
import { BeamPath } from "./BeamPath";
import { Lens } from "./Lens";
import { MainOpticLine } from "./MainOpticLine";

type LensInfo = {
  position: number;
  refractionCoeff: number;
  radiusOfCurvature: number;
  id: string;
};
type Props = {
  style?: React.HTMLAttributes<HTMLDivElement>["style"];
  lenses: ReadonlyArray<LensInfo>;
  beamVector: BeamVector;
  onLensClick?: (lensId: string) => void;
  onLineClick?: (position: number) => void;
};

export function OpticCanvas({
  style = {},
  lenses,
  beamVector,
  onLensClick,
  onLineClick,
}: Props) {
  const [beamVectorHeight] = beamVector;
  return (
    <div
      style={{
        background: "pink",
        position: "relative",
        ...style,
      }}
    >
      <div
        style={{
          position: "absolute",
          bottom: `calc(${(- beamVectorHeight + 1) * 50}% - 30px/2)`,
          left: "0",
          width: "30px",
          height: "30px",
          background: "red",
          zIndex: 2,
        }}
      />
      {lenses.map(({ position, id }) => (
        <Lens
          style={{
            position: "absolute",
            left: `calc(${position * 100}% - 15px / 2)`,
            height: "100%",
            width: "15px",
            zIndex: 2,
          }}
          onClick={() => onLensClick && onLensClick(id)}
          key={id}
        />
      ))}
      <MainOpticLine
        style={{
          width: "100%",
          height: "10px",
          position: "absolute",
          top: "calc((100% - 10px) / 2)",
          zIndex: 1,
        }}
        onClick={(ratio) => onLineClick && onLineClick(ratio)}
      />
      <BeamPath
        style={{
          width: "100%",
          height: "100%",
          position: 'absolute',
        }}
        lenses={lenses}
        beamVector={beamVector}
      />
    </div>
  );
}
