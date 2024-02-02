const { getRoot } = require('./index.js');

const consoleOutputConfig = {
	output: {
		source: console.log
	}
};


const curve1 = (x) => 1 - 1 / x;
const curveP1 = (x) => 1 / (x * x);
const curve2P1 = (x) => -2 / (x * x * x);

const root1 = getRoot(curve1, curveP1, curve2P1, 1/4, 1e-5, consoleOutputConfig);

console.log(root1, curve1(root1));
