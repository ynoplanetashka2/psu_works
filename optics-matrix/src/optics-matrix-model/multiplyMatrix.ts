export function multiplyMatrix(mat1: number[][], mat2: number[][]) {
    const res: number[][] = [];
    for (let i = 0; i < mat1.length; ++i) {
        res[i] = [];
        for (let j = 0; j < mat2.length; ++j) {
            let sum = 0;
            for (let k = 0; k in mat1[i]; ++k) {
                sum += mat1[i][k] * mat2[k][j];
            }
            res[i][j] = sum
        }
    }
    return res;
}