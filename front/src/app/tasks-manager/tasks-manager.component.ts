import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-tasks-manager',
  templateUrl: './tasks-manager.component.html',
  styleUrls: ['./tasks-manager.component.css']
})
export class TasksManagerComponent implements OnInit {

  tasks:any
  constructor(private service:SharedService) { }


  ngOnInit(): void {
    this.service.get_tasks().subscribe(d=>this.tasks=d)
  }
  deleteTask(id:number){
    this.service.delete_task(id).subscribe(
      res=>console.log(res)
    )
  }
}
