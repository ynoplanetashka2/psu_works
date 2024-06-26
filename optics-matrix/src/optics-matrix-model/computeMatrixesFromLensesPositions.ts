import { MatrixType } from "./predefined-matrix/MatrixType";
import { computeThinLensRefractionMatrix } from "./predefined-matrix/computeThinLensRefractionMatrix";
import { computeTranslateMatrix } from "./predefined-matrix/computeTranslateMatrix";

type LenseInfo = {
  position: number;
  refractionCoeff: number;
  radiusOfCurvature: number;
};
type MatrixInfo = {
  matrix: number[][];
  matrixType: MatrixType;
};
type ReturnT = MatrixInfo[];

export function computeMatrixesFromLensesPositions(
  lenses: ReadonlyArray<LenseInfo>,
  endPosition: number
): ReturnT {
  lenses = [...lenses].sort(
    ({ position: position1 }, { position: position2 }) => position1 - position2
  );
  if (lenses.length === 0) {
    return [
      {
        matrix: computeTranslateMatrix(endPosition),
        matrixType: "translateMatrix",
      },
    ];
  }
  return [
    ...lenses.flatMap((lens, index) => {
      const prevPosition = index > 0 ? lenses[index - 1].position : 0;
      const curPosition = lens.position;
      const distance = curPosition - prevPosition;
      const translateMatrix = computeTranslateMatrix(distance);
      const refractionMatrix = computeThinLensRefractionMatrix(
        lens.radiusOfCurvature,
        lens.refractionCoeff,
      );
      return [
        {
          matrix: translateMatrix,
          matrixType: "translateMatrix",
        },
        {
          matrix: refractionMatrix,
          matrixType: "thinLensRefractionMatrix",
        },
      ] as const;
    }),
    {
      matrix: computeTranslateMatrix(
        endPosition - lenses[lenses.length - 1].position
      ),
      matrixType: "translateMatrix",
    },
  ];
}
