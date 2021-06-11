import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-show-tasks',
  templateUrl: './show-tasks.component.html',
  styleUrls: ['./show-tasks.component.css']
})
export class ShowTasksComponent implements OnInit {

  tasks:any
  constructor(private service:SharedService) { }

  ngOnInit(): void {
    this.service.get_tasks().subscribe(
      data=>{
        this.tasks = data
      }
    )
  }

}
