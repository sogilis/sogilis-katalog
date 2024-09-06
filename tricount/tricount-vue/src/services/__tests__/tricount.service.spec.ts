import {describe, expect, it} from 'vitest'
import {TricountService} from "../tricount.service";

describe('TricountService', () => {
    const tricountService = new TricountService()

    it('get', () => {
       expect(tricountService.get()).toBeDefined()
    })
})