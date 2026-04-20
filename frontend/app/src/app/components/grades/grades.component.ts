import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api.service';
import { Grade } from '../../models/models';

@Component({
  selector: 'app-grades',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './grades.component.html',
  styleUrls: ['./grades.component.css']
})
export class GradesComponent {
  grades: Grade[] = [];
  errorMessage: string = '';
  isLoading: boolean = false;

  constructor(private apiService: ApiService) {}

  onLoadGrades(): void {
    this.isLoading = true;
    this.errorMessage = '';
    this.apiService.getGrades().subscribe({
      next: (data) => { this.grades = data; this.isLoading = false; },
      error: () => { this.isLoading = false; this.errorMessage = 'Ошибка загрузки оценок.'; }
    });
  }

  getGradeClass(grade: string): string {
    const num = parseFloat(grade);
    if (num >= 4.5) return 'grade-excellent';
    if (num >= 3.5) return 'grade-good';
    if (num >= 2.5) return 'grade-satisfactory';
    return 'grade-fail';
  }
}
