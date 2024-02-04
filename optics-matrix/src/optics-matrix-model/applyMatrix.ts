export function applyMatrix<Vec extends number[]>(
  matrix: number[][],
  vector: Vec
): Vec {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const result: Vec = new Array<number>(vector.length) as any;
  for (let i = 0; i < result.length; ++i) {
    result[i] = vector.reduce(
      (sum, vectorEntry, j) => sum + matrix[i][j] * vectorEntry,
      0
    );
  }
  return result;
}
