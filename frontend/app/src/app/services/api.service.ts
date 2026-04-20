import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {
  LoginRequest,
  LoginResponse,
  Course,
  ScheduleItem,
  Grade,
  Assignment,
  AssignmentCreate
} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  // Базовый URL бэкенда — меняй здесь, если URL другой
  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) {}

  // --- AUTH ---

  login(data: LoginRequest): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.baseUrl}/auth/login/`, data);
  }

  logout(): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/logout/`, {});
  }

  // --- COURSES ---

  getCourses(): Observable<Course[]> {
    return this.http.get<Course[]>(`${this.baseUrl}/courses/`);
  }

  // --- SCHEDULE ---

  getSchedule(): Observable<ScheduleItem[]> {
    return this.http.get<ScheduleItem[]>(`${this.baseUrl}/schedule/`);
  }

  // --- GRADES ---

  getGrades(): Observable<Grade[]> {
    return this.http.get<Grade[]>(`${this.baseUrl}/grades/`);
  }

  // --- ASSIGNMENTS ---

  getAssignments(): Observable<Assignment[]> {
    return this.http.get<Assignment[]>(`${this.baseUrl}/assignments/`);
  }

  createAssignment(data: AssignmentCreate): Observable<Assignment> {
    return this.http.post<Assignment>(`${this.baseUrl}/assignments/`, data);
  }

  updateAssignment(id: number, data: AssignmentCreate): Observable<Assignment> {
    return this.http.put<Assignment>(`${this.baseUrl}/assignments/${id}/`, data);
  }

  deleteAssignment(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/assignments/${id}/`);
  }
}
