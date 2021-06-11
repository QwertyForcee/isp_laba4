import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SharedService } from '../shared.service';
import { SolutionService } from '../solution.service';

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {

  task:any
  id:number = 0
  code=""

  output = ""
  status:boolean = false
  showRes = false
  get resBg(){
    return this.status?'green':'darkred'
  }
  constructor(private service:SharedService,private solutionService:SolutionService,private activateRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.id = this.activateRoute.snapshot.params['id']
    this.service.get_task(this.id).subscribe(data=>{
      this.task = data
      console.log(this.task)
    })
  }

  code_changed(ev:any){
    console.log(ev.target.value)
    this.code= ev.target.value
  }
  send(){
    if (this.code!=""){
      let solution = {
        task_id:this.id,
        source_code:this.code
      }
      this.solutionService.postSolution(solution).subscribe(
        data=>{
          this.output=data.mes
          this.status=data.status
          this.showRes=true

        }
      )
    }
  }

}
