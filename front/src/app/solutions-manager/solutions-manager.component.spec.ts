import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SolutionsManagerComponent } from './solutions-manager.component';

describe('SolutionsManagerComponent', () => {
  let component: SolutionsManagerComponent;
  let fixture: ComponentFixture<SolutionsManagerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SolutionsManagerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SolutionsManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
