export function computeTranslateMatrix(distance: number, refractiveIndex: number = 1) {
    const coeff = distance / refractiveIndex;
    return [
        [1, coeff],
        [0, 1]
    ]
}