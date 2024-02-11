import { useMeasure } from "react-use";
import { BeamVector } from "../optics-matrix-model/BeamVector";
import { useMemo } from "react";
import { computeMatrixesFromLensesPositions } from "../optics-matrix-model/computeMatrixesFromLensesPositions";
import { applyMatrix } from "../optics-matrix-model/applyMatrix";

type LensInfo = {
  position: number;
  refractionCoeff: number;
  radiusOfCurvature: number;
};
type Props = {
  style?: React.HTMLAttributes<SVGSVGElement>["style"];
  lenses: ReadonlyArray<LensInfo>;
  beamVector: BeamVector;
};

export function BeamPath({ style = {}, lenses, beamVector }: Props) {
  const [containerRef, { width, height }] = useMeasure<SVGSVGElement>();
  const transformMatrixes = useMemo(
    () => computeMatrixesFromLensesPositions(lenses, 1),
    [lenses]
  );
  const beamPositions = useMemo(() => {
    const beamPositions = new Array<{ x: number; y: number }>(
      lenses.length + 2
    );
    beamPositions[0] = {
      x: 0,
      y: beamVector[0],
    };
    let transformedBeamVector = beamVector;
    for (let i = 0; i < lenses.length; ++i) {
      const { matrix: translateMatrix } = transformMatrixes[2 * i];
      const { matrix: refractionMatrix } = transformMatrixes[2 * i + 1];
      const { position: lensePosition } = lenses[i];
      transformedBeamVector = applyMatrix(
        refractionMatrix,
        applyMatrix(translateMatrix, transformedBeamVector)
      );
      beamPositions[i + 1] = {
        x: lensePosition,
        y: transformedBeamVector[0],
      };
    }
    const { matrix: translateMatrix } =
      transformMatrixes[transformMatrixes.length - 1];
    transformedBeamVector = applyMatrix(translateMatrix, transformedBeamVector);
    beamPositions[beamPositions.length - 1] = {
      x: 1,
      y: transformedBeamVector[0],
    };
    return beamPositions;
  }, [transformMatrixes, beamVector, lenses]);
  const pathLine = useMemo(() => {
    if (!(width > 0)) {
      return "";
    }
    const initialPoint = `M${beamPositions[0].x * width} ${
      - beamPositions[0].y * height / 2 + height / 2
    }`;
    const midPath = beamPositions
      .slice(1, -1)
      .map(({ x, y }) => `L${x * width} ${y * height / 2 + height / 2}`)
      .join(" ");
    const lastPosition = beamPositions[beamPositions.length - 1];
    const endPoint = `L${lastPosition.x * width} ${
      lastPosition.y * height / 2 + height / 2
    }`;
    return `${initialPoint} ${midPath} ${endPoint}`;
  }, [width, height, beamPositions]);

  return (
    <svg style={style} ref={containerRef}>
      <path
        d={pathLine}
        style={{
          stroke: "red",
          strokeWidth: "2px",
          fill: "none",
        }}
      />
    </svg>
  );
}
