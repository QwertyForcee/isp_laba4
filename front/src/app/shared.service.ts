import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { Observable } from 'rxjs';
import { AuthService } from './auth/auth.service';


@Injectable({
  providedIn: 'root'
})
export class SharedService {
  user_id=0
  constructor(private http:HttpClient,private auth:AuthService) {
    this.auth.getAuthenticatedUser().subscribe(
      usr=>{
        this.user_id=usr.id
      }
    )
  }
  private api='http://localhost:5000/';
  private apiSign='api/v1/'

  get_somedata():Observable<any>{
    return this.http.get(this.api+'somedata')
  }
  get_task(id:number):Observable<any>{
    return this.http.get(this.apiSign+'tasks/'+id)
  }
  get_tasks():Observable<any>{
    return this.http.get(this.apiSign+'tasks')
  }
  post_task(task:any):Observable<any>{
    task['author_id']=this.user_id
    return this.http.post(this.apiSign+'tasks',task)
  }
  delete_task(id:number):Observable<any>{
    return this.http.delete(this.apiSign+'tasks/'+id)
  }
}
