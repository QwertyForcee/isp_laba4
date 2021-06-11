import { Component,HostListener, OnInit } from '@angular/core';
import {
  trigger,
  state,
  style,
  animate,
  transition
} from '@angular/animations'
import { AuthService } from '../auth/auth.service';
@Component({
  selector: 'app-main-header',
  templateUrl: './main-header.component.html',
  styleUrls: ['./main-header.component.css'],
  animations: [
    trigger('popOverState',[
      state('show',style(
        {transform: 'translateY(0)'}
      )),
      state('hide',style(
        {transform: 'translateY(-100%)'}
      )),
      transition('show => hide', animate('400ms')),
      transition('hide => show', animate('350ms'))
    ])
  ]
})
export class MainHeaderComponent implements OnInit {

  constructor(private auth:AuthService) { }

  show = true;
  oldScroll = window.scrollY
  navtop = 0
  get stateName(){
    return this.show? 'show' :'hide'
  }
  @HostListener('window:scroll', ['$event'])
  onScroll(){
    /*
    if (window.scrollY === 0){
      this.navtop = 105
    }
    else{
      this.navtop = 0
    }
    console.log(this.navtop)
    */
    this.show  = window.scrollY < this.oldScroll
    this.oldScroll = window.scrollY;
  }


  user:any
  public get isLoggedIn():boolean{
    return this.user.username != null
  }
  public get isNotLoggenIn():boolean{
    return !this.isLoggedIn //I can't use '!isLoggenIn' if *ngIf .
  }
  ngOnInit(): void {
    this.auth.getAuthenticatedUser().subscribe(u => this.user=u)
  }

  logout(){
    this.auth.logout().subscribe()
  }

}
