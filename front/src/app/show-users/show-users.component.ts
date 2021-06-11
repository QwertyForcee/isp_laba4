import { Component, OnInit } from '@angular/core';
import { UsersService } from '../users.service';

@Component({
  selector: 'app-show-users',
  templateUrl: './show-users.component.html',
  styleUrls: ['./show-users.component.css']
})
export class ShowUsersComponent implements OnInit {

  users:any
  constructor(private usersService:UsersService) { }

  ngOnInit(): void {
    this.usersService.getUsers().subscribe(res=>{
      this.users = res
    })
  }

  deleteUser(id:number){
    this.usersService.deleteUser(id).subscribe(res=>console.log(res))
  }
}
