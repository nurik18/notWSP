import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { Assignment } from '../../models/models';

@Component({
  selector: 'app-assignments',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './assignments.component.html',
  styleUrls: ['./assignments.component.css']
})
export class AssignmentsComponent implements OnInit {
  assignments: Assignment[] = [];
  errorMessage: string = '';
  successMessage: string = '';
  isLoading: boolean = false;

  title: string = '';
  description: string = '';
  dueDate: string = '';
  courseId: number = 1;

  editMode: boolean = false;
  editingId: number | null = null;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.onLoadAssignments();
  }

  onLoadAssignments(): void {
    this.isLoading = true;
    this.errorMessage = '';
    this.apiService.getAssignments().subscribe({
      next: (data) => { this.assignments = data; this.isLoading = false; },
      error: () => { this.isLoading = false; this.errorMessage = 'Ошибка загрузки заданий.'; }
    });
  }

  onCreateAssignment(): void {
    if (!this.title || !this.description) {
      this.errorMessage = 'Заполните название и описание.';
      return;
    }
    this.errorMessage = '';
    this.successMessage = '';
    this.apiService.createAssignment({ title: this.title, description: this.description, due_date: this.dueDate, course_id: this.courseId }).subscribe({
      next: (newA) => { this.assignments.push(newA); this.successMessage = 'Задание создано!'; this.clearForm(); },
      error: () => { this.errorMessage = 'Ошибка при создании задания.'; }
    });
  }

  onDeleteAssignment(id: number): void {
    if (!confirm('Удалить задание?')) return;
    this.apiService.deleteAssignment(id).subscribe({
      next: () => { this.assignments = this.assignments.filter(a => a.id !== id); this.successMessage = 'Задание удалено.'; },
      error: () => { this.errorMessage = 'Ошибка при удалении.'; }
    });
  }

  onEditAssignment(assignment: Assignment): void {
    this.editMode = true;
    this.editingId = assignment.id;
    this.title = assignment.title;
    this.description = assignment.description;
    this.dueDate = assignment.due_date;
    this.courseId = assignment.course_id;
  }

  onSaveEdit(): void {
    if (!this.title || !this.description || this.editingId === null) return;
    this.apiService.updateAssignment(this.editingId, { title: this.title, description: this.description, due_date: this.dueDate, course_id: this.courseId }).subscribe({
      next: (updated) => {
        const i = this.assignments.findIndex(a => a.id === this.editingId);
        if (i !== -1) this.assignments[i] = updated;
        this.successMessage = 'Задание обновлено!';
        this.cancelEdit();
      },
      error: () => { this.errorMessage = 'Ошибка при обновлении.'; }
    });
  }

  cancelEdit(): void {
    this.editMode = false;
    this.editingId = null;
    this.clearForm();
  }

  clearForm(): void {
    this.title = '';
    this.description = '';
    this.dueDate = '';
    this.courseId = 1;
  }
}
