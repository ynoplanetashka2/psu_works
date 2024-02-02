//@ts-check

import { range } from 'range'

/**
 * @template T
 * @typedef {{action: T, priority: number}} ScheduledAction
 */
/**
 * @template T
 */
export class ActionScheduler {
	/**
     * @type {number}
     */
	#currentDay = 0
	/**
     * @type {Map<number, ScheduledAction<T>>}
     */
	#scheduledActions = new Map()

	/**
     * schedule an action
     * @param {T} action 
     * @param {number} priority 
     */
	schedule(action, priority, day) {
		if (day > this.#currentDay) {
			throw new Error(`current day is greater than day on which scheduling attempted`)
		}
		let possibleDays = range(this.#currentDay, day)
		for (const [day, { priority: scheduledItemPriority }] of this.#scheduledActions.entries()) {
			if (
				possibleDays.includes(day)
                && priority <= scheduledItemPriority
			) {
				possibleDays = possibleDays.filter(possibleDay => possibleDay !== day)
			}
		}
		if (possibleDays.length === 0) {
			throw new Error(`day can not be scheduled`)
		}
		const appropriateDay = possibleDays[possibleDays.length - 1]
		this.#scheduledActions.set(appropriateDay, { action, priority })
	}
    
	/**
     * get sceduled actions for a certain day
     * @param {number} day 
     */
	resolve(day) {
		this.#currentDay = day
		return this.#scheduledActions.get(day)?.action ?? null
	}

	/**
     * @returns {ActionScheduler}
     */
	clone() {
		const scheduler =  new ActionScheduler()
		scheduler.#currentDay = this.#currentDay
		scheduler.#scheduledActions = new Map(this.#scheduledActions)
		return scheduler
	}
}