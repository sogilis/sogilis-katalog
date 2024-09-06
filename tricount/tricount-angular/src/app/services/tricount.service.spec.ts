import { TestBed } from '@angular/core/testing';

import { TricountService } from './tricount.service';

describe('TricountService', () => {
  let service: TricountService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TricountService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
