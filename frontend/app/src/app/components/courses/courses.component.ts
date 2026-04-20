import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api.service';
import { Course } from '../../models/models';

@Component({
  selector: 'app-courses',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css']
})
export class CoursesComponent {
  courses: Course[] = [];
  errorMessage: string = '';
  isLoading: boolean = false;

  constructor(private apiService: ApiService) {}

  onLoadCourses(): void {
    this.isLoading = true;
    this.errorMessage = '';
    this.apiService.getCourses().subscribe({
      next: (data) => { this.courses = data; this.isLoading = false; },
      error: () => { this.isLoading = false; this.errorMessage = 'Ошибка загрузки курсов.'; }
    });
  }
}
