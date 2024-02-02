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

function* flatRange(x1, y1, x2, y2, step = 1) {
	[[x1, y1], [x2, y2]] = mainDiagonalPoints(x1, y1, x2, y2);
	let curPos = [x1, y1];
	for (let i = x1; i <= x2; i += step) {
		for (let j = y1; j >= y2; j -= step) {
			yield [i, j];
		}
	}
}

function* circuitRange(x1, y1, x2, y2, step = 1) {
	[[x1, y1], [x2, y2]] = mainDiagonalPoints(x1, y1, x2, y2);
	let curPos = [x1, y1];

	while (curPos[1] > y2) {
		yield curPos;
		curPos[1] -= step;
	}
	while (curPos[0] < x2) {
		yield curPos;
		curPos[0] += step;
	}
	while (curPos[1] < y1) {
		yield curPos;
		curPos[1] += step;
	}
	while (curPos[0] > x1) {
		yield curPos;
		curPos[0] -= step;
	}
}

function* joinIters(...iters) {
	for (const iter of iters) {
		yield* iter;
	}
}

const time = 1e4;
const position = [9, 7.5];

const L = 10;
const H = 10;

const XI = 1e-3;

const boundaryTemp = 0;
const midTemp = 1;
const initialTemp = .5;

const coordStep = 3.3e-1;
const timeStep = coordStep**2 / 4;

function getIndexesByCoord(x, y) {
	return [Math.ceil(x / coordStep), Math.ceil(y / coordStep)];
}

function getCoordByIndexes(i, j) {
	return [coordStep * i, coordStep * j];
}
const positionIndexes = getIndexesByCoord(...position);

const [elementsInWidth, elementsInHeight] = getIndexesByCoord(L, H).map(i => i + 1);

const midPoint = getIndexesByCoord(L / 2, H / 2);
const [midX, midY] = midPoint;

let curState = new Array(elementsInHeight).fill(undefined).map(() => new Array(elementsInHeight).fill(initialTemp));
curState[midX][midY] = midTemp;
for (const [i, j] of circuitRange(0, 0, elementsInWidth - 1, elementsInHeight - 1)) curState[i][j] = boundaryTemp;
// console.log(curState);
let futState = new Array(elementsInHeight).fill(undefined).map(() => new Array(elementsInHeight).fill(undefined));

for (const curTime of range(0, time, timeStep)) {
    const produceState = (i, j) => {
        return curState[i][j] + XI * (timeStep / coordStep**2) * ((curState[i + 1][j] - 2*curState[i][j] + curState[i - 1][j]) + (curState[i][j + 1] - 2*curState[i][j] + curState[i][j - 1]));
    }
	for (const [i, j] of flatRange(1, 1, elementsInWidth - 2, elementsInHeight - 2)) {
		futState[i][j] = produceState(i, j);
	}
	for (const [i, j] of circuitRange(0, 0, elementsInWidth - 1, elementsInHeight - 1)) {
		if (i % (elementsInWidth - 1) === 0 && j % (elementsInHeight - 1) === 0) continue;
        if (i % (elementsInWidth - 1) === 0) futState[i][j] = 0;
        if (j % (elementsInHeight - 1) === 0) futState[i][j] = futState.at(-elementsInHeight);
		// if (i === 0) futState[i][j] = futState[i + 1][j];
		// if (j === elementsInHeight - 1) futState[i][j] = futState[i][j - 1];
		// if (i === elementsInWidth - 1) futState[i][j] = 0;
		// if (j === 0 && i >= midX) futState[i][j] = futState[i][j + 1];
		// if (j === 0 && i < midX) futState[i][j] = 1;
	}

	[curState, futState] = [futState, curState];
}

curState[0][0] = (curState[1][0] + curState[0][1]) / 2;
curState[elementsInWidth - 1][0] = (curState[elementsInWidth - 1][1] + curState[elementsInWidth - 2][0]) / 2;
curState[0][elementsInHeight - 1] = (curState[1][elementsInHeight - 1] + curState[0][elementsInHeight - 2]) / 2;
curState[elementsInWidth - 1][elementsInHeight - 1] = (curState[elementsInWidth - 2][elementsInHeight - 1] + curState[elementsInWidth - 1][elementsInHeight - 2]) / 2;

/*
curState[0][0] = curState[0][1];
curState[elementsInWidth - 1][0] = curState[elementsInWidth - 2][0];
curState[0][elementsInHeight - 1] = curState[0][elementsInHeight - 2];
curState[elementsInWidth - 1][elementsInHeight - 1] = curState[elemenentsInWidth - 2][elementsInHeight - 1];
*/

const _3DMap = [];
for (const [i, j] of flatRange(0, 0, elementsInWidth - 1, elementsInHeight - 1)) {
	_3DMap.push([...getCoordByIndexes(i, j), curState[i][j]]);
}
const data = _3DMap.reduce((acc, [x, y, z]) => acc + `${x} ${y} ${z}\n`, '');

fs.writeFileSync('./output.txt', data);
