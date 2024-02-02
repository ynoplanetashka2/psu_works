export function computeThinLensRefractionMatrix(radiusOfCurvature: number, n1: number = 1, n2: number = n1) {
    const coeff = (n1 - n2) / radiusOfCurvature;
    return [
        [1, coeff],
        [0, 1]
    ]
}