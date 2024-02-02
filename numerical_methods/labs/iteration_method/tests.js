const { transformFromStandart, getFixedPoint } = require('./index.js');

const consoleOutputConfig = {
	output: {
		source: console.log
	}
};

const curve1 = (x) => 1 / x - 1;
const transformed1 = transformFromStandart(curve1, -5);

const fixed1 = getFixedPoint(transformed1, 1/4, 2, 1e-3/5, 1.5, consoleOutputConfig, curve1);
console.log(fixed1, curve1(fixed1));
