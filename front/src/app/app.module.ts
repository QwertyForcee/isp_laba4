import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TaskComponent } from './task/task.component';
import { HomeComponent } from './home/home.component';
import { AuthComponent } from './auth/auth.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ShowTasksComponent } from './show-tasks/show-tasks.component';
import { MainHeaderComponent } from './main-header/main-header.component';
import { AdminPanelComponent } from './admin-panel/admin-panel.component';
import { SolutionsManagerComponent } from './solutions-manager/solutions-manager.component';
import { TaskCreatorComponent } from './task-creator/task-creator.component';
import { ShowUsersComponent } from './show-users/show-users.component';
import { TasksManagerComponent } from './tasks-manager/tasks-manager.component';


@NgModule({
  declarations: [
    AppComponent,
    TaskComponent,
    HomeComponent,
    AuthComponent,
    ShowTasksComponent,
    MainHeaderComponent,
    AdminPanelComponent,
    SolutionsManagerComponent,
    TaskCreatorComponent,
    ShowUsersComponent,
    TasksManagerComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
