export function computeThinLensRefractionMatrix(
  radiusOfCurvature: number,
  n1: number = 1,
  n2: number = 1
) {
  const coeff = (n1 - n2) / radiusOfCurvature;
  return [
    [1, 0],
    [coeff, 1],
  ];
}
