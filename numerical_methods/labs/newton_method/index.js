const makeStep = (curve, curveP, x) => x - (curve(x) / curveP(x));

module.exports.getRoot = function getRoot(curve, curveP, curve2P, startValue, errorRange, config) {
	const writeOutput = config?.output?.source;

	let currentValue = startValue;
	let iterationCount = 0;

	while (Math.abs(curve(currentValue)) > errorRange) {
		if (curve(currentValue) * curve2P(currentValue) < 0) throw new Error(`invalid function (curve*curve2P < 0)`);
		if (writeOutput) writeOutput(`curValue = ${currentValue}; iteration = ${iterationCount}, funcValue = ${curve(currentValue)}`);
		iterationCount++;
		currentValue = makeStep(curve, curveP, currentValue);
	}

	return currentValue;
};
