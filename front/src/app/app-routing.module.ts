import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminPanelComponent } from './admin-panel/admin-panel.component';
import { AdminGuard } from './admin-panel/admin.guard';
import { AuthComponent } from './auth/auth.component';
import { AuthGuard } from './auth/auth.guard';
import { HomeComponent } from './home/home.component';
import { ShowTasksComponent } from './show-tasks/show-tasks.component';
import { ShowUsersComponent } from './show-users/show-users.component';
import { SolutionsManagerComponent } from './solutions-manager/solutions-manager.component';
import { TaskCreatorComponent } from './task-creator/task-creator.component';
import { TaskComponent } from './task/task.component';
import { TasksManagerComponent } from './tasks-manager/tasks-manager.component';

const adminRoutes: Routes = [
  {path:'solutions',component:SolutionsManagerComponent},
  {path:'newtask',component:TaskCreatorComponent},
  {path:'users',component:ShowUsersComponent},
  {path:'tasks',component:TasksManagerComponent}
]
const routes: Routes = [
  {path:'home',component:HomeComponent},
  {path:"auth",component:AuthComponent},
  {path:"tasks",canActivate:[AuthGuard],component:ShowTasksComponent},
  {path:"task/:id",component:TaskComponent},
  {path:"admin",canActivate:[AdminGuard],component:AdminPanelComponent,children:adminRoutes}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
