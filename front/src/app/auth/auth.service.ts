import { Injectable } from '@angular/core';
import {FormGroup} from '@angular/forms';
import {Observable, Subject, throwError} from 'rxjs';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import {catchError, map, take} from 'rxjs/operators';
import {tap} from 'rxjs/internal/operators/tap';
import {Router} from '@angular/router';

export class UserModel {
  id: number;
  username: string;
  email: string;
  role: string|null;

  constructor(id: number, username: string, email: string,role: string|null) {
    this.id = id;
    this.username = username;
    this.email = email;
    this.role = role
  }

}

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  authenticationChanged = new Subject();
  constructor(private http: HttpClient, private router: Router) {
  }

  api = "http://localhost:5000/"
  private handleAuthentication(): void {
    window.setTimeout(() => {
      this.authenticationChanged.next();
      this.router.navigate(['/tasks']);
    }, 2000);

  }

  login(form: FormGroup): Observable<any> {
    let data = {
      username: form.value.user_login,
      password: form.value.password
    }
    const headers = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
    //const headers = new HttpHeaders();
    //headers.append('Content-Type', 'application/json');
    //headers.append('Accept', 'application/json');
    console.log(data)
    return this.http.post<any>("api/v1/login", data, {headers: headers})
    //return this.http.post<JSON>(this.api+'login',JSON.stringify(data) )
      .pipe(
        catchError(this.handleError),
        tap(resData => {
          this.handleAuthentication();
        })
      );
  }

  logout(): Observable<any> {
    return this.http.post<any>('api/v1/log_out', {})
      .pipe(
        catchError(this.handleError),
        tap(resData => {
          this.authenticationChanged.next();
          this.router.navigate(['/']);
        })
      );
  }

  register(form: FormGroup): Observable<any> {
    console.log({
      username: form.value.user,
      password: form.value.password_1,
      email: form.value.email_address1
    })
    const headers = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
    return this.http.post<string>('api/v1/register', {
      username: form.value.user,
      password: form.value.password_1,
      email: form.value.email_address1
    },
    {headers:headers})
      .pipe(
        catchError(this.handleError),
        tap(resData => {
          this.handleAuthentication();
        })
      );
  }

  getAuthenticatedUser(): Observable<UserModel>  {
    return this.http.get<any>('api/v1/users/current', {})
      .pipe(
        catchError(this.handleError),
        take(1),
        map(resp => {
          console.log(resp)
          return new UserModel(resp.response.data.user_id, resp.response.data.username, resp.response.data.email,resp.response.data.role);
        })
      );
  }

  private handleError(errorRes: HttpErrorResponse): Observable<any> {
    let errorMessage = 'An unknown error occurred!';
    if (!errorRes.error ||
      !errorRes.error.response) {
      return throwError(errorMessage);
    }

    if (errorRes.error.response.error) {
      return throwError(errorRes.error.response.error);

    } else if (errorRes.error.response.errors) {

      const errorObj = errorRes.error.response.errors;

      for (const prop in errorObj) {
        if (errorObj.hasOwnProperty(prop)) {
          errorMessage = errorObj[prop];
        }
      }
    }

    return throwError(errorMessage);
  }
}
