import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedService {

  constructor(private http:HttpClient) { }
  private api='http://localhost:5000/';

  get_somedata():Observable<any>{
    return this.http.get(this.api+'somedata')
  }
  get_task(id:number):Observable<any>{
    return this.http.get('tasks/'+id)
  }

}
