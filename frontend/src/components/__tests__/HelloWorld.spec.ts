import { describe, it, expect,test } from 'vitest'

import { mount } from '@vue/test-utils'
import { calcul_prix_tva_inclu } from '@/utils';

test('100 should be 120', () => {
  expect(calcul_prix_tva_inclu(100)).toBe(120);
});