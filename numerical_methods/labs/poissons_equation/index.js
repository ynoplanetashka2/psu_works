const fs = require('fs');

function* range(...args) {
	let from, to, step;
	switch (args.length) {
		case 1:
			from = 0;
			to = args[0];
			step = 1;
			break;
		case 2:
			from = args[0];
			to = args[1];
			step = 1;
			break;
		case 3:
			from = args[0];
			to = args[1];
			step = args[2];
			break;
	}

	for (let i = from; i < to; i += step) {
		yield i;
	}
}

// returns top left and right bottom points(ordered)
function mainDiagonalPoints(x1, y1, x2, y2) {
	if (x1 < x2) {
		if (y1 < y2) {
			return [
				[x1, y2],
				[x2, y1]
			];
		}
		return [
			[x1, y1],
			[x2, y2]
		];
	}
	if (y1 < y2) {
		return [
			[x2, y2],
			[x1, y1]
		];
	}
	return [
		[x2, y1],
		[x1, y2]
	];
}

function* flatRange (x1, y1, x2, y2, step = 1) {
	[[x1, y1], [x2, y2]] = mainDiagonalPoints(x1, y1, x2, y2);
	let curPos = [x1, y1];
	for (let i = x1; i < x2; i += step) {
		for (let j = y1; j > y2; j -= step) {
			yield [i, j];
		}
	}
}

const coordStep = 1.5e-1;
const timeStep = coordStep**2 / 4;

const preciseness = 1e-2;

const L = 10;
const H = 30;

const n = 2;
const m = 3;

const initialState = (x, y) => 0;
const chargeDistributionFunction = (x, y) => Math.sin(Math.PI * n * x / L) * Math.sin(Math.PI * m * y / H);

const boundaryPotential = 0;

const coef1 = timeStep / coordStep ** 2;
const coef2 = timeStep / coordStep ** 2;
const coef3 = 4 * Math.PI * timeStep;

function getIndexesByCoord(x, y) {
	return [Math.ceil(x / coordStep), Math.ceil(y / coordStep)];
}

function getCoordByIndexes(i, j) {
	return [coordStep * i, coordStep * j];
}

const [elementsInWidth, elementsInHeight] = getIndexesByCoord(L, H).map(i => i + 1);

let curState = new Array(elementsInWidth).fill(undefined).map(() => new Array(elementsInHeight).fill(0));
let newState = new Array(elementsInWidth).fill(undefined).map(() => new Array(elementsInHeight).fill(0));

const chargeDistr = new Array(elementsInWidth).fill(undefined).map(() => new Array(elementsInHeight).fill(undefined));
for (const [i, j] of flatRange(0, 0, elementsInWidth - 1, elementsInHeight - 1)) {
	const [x, y] = getCoordByIndexes(i, j);
	chargeDistr[i][j] = chargeDistributionFunction(x, y);
}

let error = Infinity;
let iterCount = 0;
const step = () => {
	let newState = new Array(elementsInWidth).fill(undefined).map(() => new Array(elementsInHeight).fill(boundaryPotential));
	for (const [i, j] of flatRange(1, 1, elementsInWidth - 2, elementsInHeight - 2)) {
		newState[i][j] = curState[i][j] + coef1 * (curState[i + 1][j] - 2*curState[i][j] + curState[i - 1][j]) + coef2 * (curState[i][j + 1] - 2*curState[i][j] + curState[i][j - 1]) + coef3 * chargeDistr[i][j];
	}

	let maxError = 0;
	for (const [i, j] of flatRange(1, 1, elementsInWidth - 2, elementsInHeight - 2)) {
		curError = Math.abs(newState[i][j] - curState[i][j]);
		if (maxError < curError) maxError = curError;
	}
	error = maxError;

	[curState, newState] = [newState, curState];
	iterCount++;
	// console.log(error);
}

while (error > preciseness) step();

const midPoint = getIndexesByCoord(L / 2, H / 2);
const [midX, midY] = midPoint;

const _3DMap = [];
for (const [i, j] of flatRange(0, 0, elementsInWidth - 1, elementsInHeight - 1)) {
	_3DMap.push([...getCoordByIndexes(i, j), curState[i][j]]);
}

const txtOutput = _3DMap.reduce((acc, [x, y, z]) => acc + `${x} ${y} ${z}\n`, '');
fs.writeFileSync('./output.txt', txtOutput);

