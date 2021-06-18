import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from './auth/auth.service';

@Injectable({
  providedIn: 'root'
})
export class SolutionService {

  constructor(private http:HttpClient,private auth:AuthService) {
    this.auth.getAuthenticatedUser().subscribe(usr=>{
      this.user_id=usr.id
    })

   }
  private apiSign='api/v1/'
  private user_id=0
  postSolution(solution:any):Observable<any>{

    //solution.user_id=this.user_id
    console.log(solution)
    solution.user_id = this.user_id
    return this.http.post(this.apiSign+'post_solution',solution)
  }
  getSolutions():Observable<any>{
    return this.http.get(this.apiSign+'solutions')
  }
  deleteSolution(id:any):Observable<any>{
    return this.http.delete(this.apiSign+'solutions/'+id)
  }

}
