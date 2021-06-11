import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-task-creator',
  templateUrl: './task-creator.component.html',
  styleUrls: ['./task-creator.component.css']
})
export class TaskCreatorComponent implements OnInit {

  constructor(private service:SharedService) {
    this.taskForm = new FormGroup({
      "title":new FormControl("",Validators.required),
      "description":new FormControl("",Validators.required),
      "tests":new FormControl("",Validators.required)
    })
  }
  taskForm:FormGroup

  ngOnInit(): void {
  }

  submit(){
    console.log(this.taskForm.value)
    let o = this.taskForm.value
    this.service.post_task(o).subscribe(r=>console.log(r))
  }
}
