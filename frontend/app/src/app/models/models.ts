// Интерфейсы для всех данных приложения

export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  access: string;   // JWT access token
  refresh?: string; // JWT refresh token (опционально)
}

export interface Course {
  id: number;
  name: string;
  teacher: string;
  credits: number;
}

export interface ScheduleItem {
  id: number;
  course_name: string;
  day: string;
  time: string;
  room: string;
}

export interface Grade {
  id: number;
  course_name: string;
  grade: string;
  date: string;
}

export interface Assignment {
  id: number;
  title: string;
  description: string;
  due_date: string;
  course_id: number;
  is_completed: boolean;
}

export interface AssignmentCreate {
  title: string;
  description: string;
  due_date: string;
  course_id: number;
}
