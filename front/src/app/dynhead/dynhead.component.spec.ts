import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DynheadComponent } from './dynhead.component';

describe('DynheadComponent', () => {
  let component: DynheadComponent;
  let fixture: ComponentFixture<DynheadComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DynheadComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DynheadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
