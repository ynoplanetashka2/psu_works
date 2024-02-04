export function applyMatrix(matrix: number[][], vector: number[]) {
  const result = new Array(vector.length);
  for (let i = 0; i < result.length; ++i) {
    result[i] = vector.reduce((vectorEntry, j) => matrix[i][j] * vectorEntry);
  }
  return result;
}
