module.exports.transformFromStandart = function transformFromStandart(curve, divisionCoefficient = 1) {
	return (x) => x - curve(x) / divisionCoefficient;
};

module.exports.getFixedPoint = function getFixedPoint(curve, leftBound, rightBound, errorRange, startValue = leftBound, config, func) {
	const writeOutput = config?.output?.source;
	let previousValue = startValue;
	let currentValue = curve(previousValue);
	let iterationCount = 0;

	if (currentValue > rightBound) {
		currentValue = rightBound;
	}

	while (Math.abs(currentValue - previousValue) > errorRange) {
		if (writeOutput) writeOutput(`prevValue = ${previousValue}; curValue = ${currentValue}; iteration# = ${iterationCount}, funcValue = ${func ? func(currentValue) : "not defined"}`);
		iterationCount++;
		previousValue = currentValue;
		currentValue = curve(currentValue);
	}

	return currentValue;
};
