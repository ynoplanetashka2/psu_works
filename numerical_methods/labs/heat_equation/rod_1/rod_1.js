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

const time = 1e4;
// const position = 0.15;

const L = 10;
const XI = 1e-3;
const n = 1;

const boundaryValue = 1;
const initialState = (x) => 0;

const coordStep = 1e-1;
const timeStep = 1e-1;

function indexFromCoord(stepSize, coord) {
	return Math.ceil(coord / stepSize);
}

function coordFromIndex(stepSize, index) {
	return stepSize * index;
}

const elementsCount = indexFromCoord(coordStep, L) + 1;
let curState = [];
let futState = [];

curState[0] = boundaryValue;
for (const i of range(1, elementsCount)) {
	curState[i] = initialState(coordFromIndex(i));
}

// let domain = [];
// let values = [];
for (const curTime of range(0, time + timeStep, timeStep)) {
	// domain.push(curTime);
	futState[0] = boundaryValue;
	for (const i of range(1, elementsCount - 1)) {
		futState[i] = curState[i] + XI * (timeStep / coordStep**2) * (curState[i + 1] - 2 * curState[i] + curState[i - 1]);
	}
	futState[elementsCount - 1] = futState[elementsCount - 2];
	
	[curState, futState] = [futState, curState];
	// values.push(curState[indexFromCoord(coordStep, position)]);
}

let domain = futState.map((_, index) => coordFromIndex(coordStep, index));
let values = futState;

// const queryObject = {
//   type: 'line',
//   data: {
//     labels: domain.map(val => Math.round(10*val)/10).filter((_, ind) => ind % 1000 === 0),
//     datasets: [{
//       label: 'curve',
//       data: values.map(val => val).filter((_, ind) => ind % 1000 === 0),
//       fill: false,
//       borderColor: 'green',
//       backgroundColor: 'green',
//     }]
//   }
// };
// const query = JSON.stringify(queryObject);
// console.log(query);

const pointsCount = 1e2;
const queryObject = {
  type: 'line',
  data: {
    labels: domain.map(val => Math.round(10*val)/10).filter((_, ind) => ind % Math.round(domain.length / pointsCount) === 0),
    datasets: [{
      label: 'curve',
      data: values.map(val => val).filter((_, ind) => ind % Math.round(domain.length / pointsCount) === 0),
      fill: false,
      borderColor: 'green',
      backgroundColor: 'green',
    }]
  }
};
const query = JSON.stringify(queryObject);
console.log(query);