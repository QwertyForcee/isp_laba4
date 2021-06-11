import { Component, OnInit } from '@angular/core';
import { SolutionService } from '../solution.service';

@Component({
  selector: 'app-solutions-manager',
  templateUrl: './solutions-manager.component.html',
  styleUrls: ['./solutions-manager.component.css']
})
export class SolutionsManagerComponent implements OnInit {

  solutions:any;
  constructor(private solutionService:SolutionService) { }

  ngOnInit(): void {
    this.solutionService.getSolutions().subscribe(data=>{
      this.solutions = data
    })
  }
  deleteSolution(id:number){
    this.solutionService.deleteSolution(id).subscribe(
      res=>console.log(res)
    )
  }

}
