import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import Tricount from '../Tricount.vue'

describe('Tricount', () => {
  it('renders properly', () => {
    const wrapper = mount(Tricount)
    expect(wrapper.text()).toContain('Tricount')
  })
})
