//@ts-check
import { ActionScheduler } from './ActionScheduler'

const DAY_RESULT = {
	NONE: 0,
	HAPPY_END: 1,
	DEAD_END: 2,
}
const RESIDENCE_NAME = {
	NONE: 0,
	HUT: 1,
	CAVE: 2,
}
const FOOD_TYPE = {
	NONE: 0,
	VEGAN: 1,
	FISH: 2,
	GAME: 3,
}

const MONTH_TIME = 25
const MAX_DAYS = 12 * MONTH_TIME
const CAVE_BUILD_TIME = 15
const CAVE_MAINTAIN_PERIOD = 1 * MONTH_TIME
const CAVE_MAINTAIN_TIME = 1
const CAVE_REPAIR_PERIOD = 3 * MONTH_TIME
const CAVE_REPAIR_TIME = 4
const HUT_BUILD_TIME = 4
const HUT_MAINTAIN_PERIOD = MONTH_TIME
const HUT_MAINTAIN_TIME = 4
const OLD_CLOTHES_MAINTAIN_PERIOD = MONTH_TIME
const OLD_CLOTHES_MAINTAIN_TIME = 3
const NEW_CLOTHES_MADE_TIME = 5
const NEW_CLOTHES_MAINTAIN_PERIOD = MONTH_TIME
const NEW_CLOTHES_MAINTAIN_TIME = 1
const NEW_CLOTHES_REPAIR_PERIOD = 3 * MONTH_TIME
const NEW_CLOTHES_REPAIR_TIME = 2
const VEGAN_FOOD_PROVIDED_TIME = 3
const GAME_PROVIDED_TIME = 10
const FISH_PROVIDED_TIME = 5
const DISTINCT_FOOD_PERIOD = 25
const HUNTING_TOOLS_MADE_TIME = 20
const HUNTING_TOOLS_REPAIR_TIME = 2
const HUNTING_TOOLS_USES_COUNT = 5
const FISHNET_MADE_TIME = 10
const FISHNET_REPAIR_TIME = 5
const FISHNET_USES_COUNT = 5
const RAFT_BUILD_TIME = 100

const CONTEXT = {
	currentDay: 0,
	get untilEnd() {
		return MAX_DAYS - this.currentDay
	},
	get isEnded() {
		return this.untilEnd === 0
	},
	currentResidence: RESIDENCE_NAME.NONE,
	cave: {
		leftToBuild: CAVE_BUILD_TIME,
		get isBuild() {
			return this.leftToBuild === 0
		},
		untilNextMaintain: CAVE_MAINTAIN_PERIOD,
		leftToMaintain: CAVE_MAINTAIN_TIME,
		untilNextRepair: CAVE_REPAIR_PERIOD,
		leftToRepair: CAVE_REPAIR_TIME,
	},
	hut: {
		leftToBuild: HUT_BUILD_TIME,
		get isBuild() {
			return this.leftToBuild === 0
		},
		untilNextMaintain: HUT_MAINTAIN_PERIOD,
		leftToMaintain: HUT_MAINTAIN_TIME,
	},
	oldClothes: {
		untilNextMaintain: OLD_CLOTHES_MAINTAIN_PERIOD,
	},
	newClothes: {
		leftToMade: NEW_CLOTHES_MADE_TIME,
		get isMade() {
			return this.leftToMade === 0
		},
		untilNextMaintain: NEW_CLOTHES_MAINTAIN_PERIOD,
		untilNextRepair: NEW_CLOTHES_REPAIR_PERIOD,
	},
	huntingTools: {
		leftToMade: HUNTING_TOOLS_MADE_TIME,
		get isMade() {
			return this.leftToMade === 0
		},
		usesLeft: HUNTING_TOOLS_USES_COUNT,
	},
	fishnet: {
		leftToMade: FISHNET_MADE_TIME,
		get isMade() {
			return this.leftToMade === 0
		},
		usesLeft: FISHNET_USES_COUNT,
	},
	accamulatedVeganFood: 0,
	accamulatedFish: 0,
	accamulatedGame: 0,
	lastEatenFoodType: FOOD_TYPE.NONE,
	untilNextDistinctFood: DISTINCT_FOOD_PERIOD,
	get totalFood() {
		return (
			this.vegan_food.accamulated
			+ this.fishnet.accamulated
			+ this.huntingTools.accamulated
		)
	},
	leftToBuildRaft: RAFT_BUILD_TIME,
	actionsScheduler: new ActionScheduler()
}
/**
 * @typedef {typeof CONTEXT} Context
 */
/**
 * @typedef {(ctx: Context) => (typeof DAY_RESULT)[keyof typeof DAY_RESULT]} ActionType
 */

/**
 * @type {{[key: string]: ActionType}} ACTIONS
 */
const ACTIONS = {
	COLLECT_VEGAN_FOOD: ctx => {
		const foodType = FOOD_TYPE.VEGAN
		ctx.accamulatedVeganFood += VEGAN_FOOD_PROVIDED_TIME
		const { lastEatenFoodType } = ctx
		if (lastEatenFoodType === foodType) {
			ctx.untilNextDistinctFood--
		}
		else {
			ctx.lastEatenFoodType = foodType
			ctx.untilNextDistinctFood = DISTINCT_FOOD_PERIOD
		}
		return DAY_RESULT.NONE
	}
}

/**
 * @param {Context} ctx 
 */
const isValidCtx = ctx => {
	return !!ctx
}
/**
 * @param {Context} ctx 
 * @param {any} actions
 */
const getHappyEndings = function* (ctx, actions) {
	// const shuffledActions = shuffleArray(ACTIONS_LIST, { copy: true })
	/**
	 * @type {string[]}
	 */
	const playedActions = []
	for (const actionsName in actions) {
		const action = ACTIONS[actionsName]
		const actionResult = action(ctx)
		switch (actionResult) {
			case DAY_RESULT.NONE:
				if (ctx.isEnded) {
					return
				}
				playedActions.push(actionsName)
				break
			case DAY_RESULT.HAPPY_END:
				yield playedActions
				break
			case DAY_RESULT.DEAD_END:
				return
		}
	}
}

/**
 * @param {Context} ctx 
 * @param {any} actions
 */
const main = (ctx, actions) => {
	for (const happyEnd of getHappyEndings(ctx, actions)) {
		console.log(happyEnd)
	}
}
main(CONTEXT, ACTIONS)