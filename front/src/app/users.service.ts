import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  apiSign = 'api/v1/'
  constructor(private http:HttpClient) { }
  getUsers():Observable<any>{
    return this.http.get(this.apiSign+'users')
  }
  deleteUser(id:number):Observable<any>{
    return this.http.delete(this.apiSign+'users/'+id)
  }
}
