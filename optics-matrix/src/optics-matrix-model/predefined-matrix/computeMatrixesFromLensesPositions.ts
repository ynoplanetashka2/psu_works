import { MatrixType } from "./MatrixType";
import { computeThinLensRefractionMatrix } from "./computeThinLensRefractionMatrix";
import { computeTranslateMatrix } from "./computeTranslateMatrix";

type LenseInfo = {
  position: number;
  radiusOfCurvature: number;
};
type MatrixInfo = {
  matrix: number[][];
  matrixType: MatrixType;
};
type ReturnT = MatrixInfo[];

export function computeMatrixesFromLensesPositions(
  lenses: ReadonlyArray<LenseInfo>
): ReturnT {
  lenses = [...lenses].sort(
    ({ position: position1 }, { position: position2 }) => position1 - position2
  );
  return lenses.flatMap((lens, index) => {
    const prevPosition = index > 0 ? lenses[index - 1].position : 0;
    const curPosition = lens.position;
    const distance = curPosition - prevPosition;
    const translateMatrix = computeTranslateMatrix(distance);
    const refractionMatrix = computeThinLensRefractionMatrix(
      lens.radiusOfCurvature,
      // @TODO: remove hardcoded refraction index
      1.1
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
    ];
  });
}
