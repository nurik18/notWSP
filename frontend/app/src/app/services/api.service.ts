import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class ApiService {

  private baseUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  login(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/login/`, data);
  }

   getCourses(): Observable<any> {
    return this.http.get(`${this.baseUrl}/courses/`);
  }

  getSchedule(): Observable<any> {
    return this.http.get(`${this.baseUrl}/schedule/`);
  }

    getGrades(): Observable<any> {
    return this.http.get(`${this.baseUrl}/grades/`);
  }

  getAssignments(): Observable<any> {
    return this.http.get(`${this.baseUrl}/assignments/`);
  }

   createAssignment(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/assignments/`, data);
  }

  updateAssignment(id: number, data: any): Observable<any> {
    return this.http.put(`${this.baseUrl}/assignments/${id}/`, data);
  }

  deleteAssignment (id: number): Observable <any> {
    return this.http.delete(`${this.baseUrl}/assignments/${id}`)
  }
}