export function computeDeterminant(matrix: number[][]) {
    const det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1];
    return det;
}