import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api.service';
import { ScheduleItem } from '../../models/models';

@Component({
  selector: 'app-schedule',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css']
})
export class ScheduleComponent {
  schedule: ScheduleItem[] = [];
  errorMessage: string = '';
  isLoading: boolean = false;

  constructor(private apiService: ApiService) {}

  onLoadSchedule(): void {
    this.isLoading = true;
    this.errorMessage = '';
    this.apiService.getSchedule().subscribe({
      next: (data) => { this.schedule = data; this.isLoading = false; },
      error: () => { this.isLoading = false; this.errorMessage = 'Ошибка загрузки расписания.'; }
    });
  }
}
