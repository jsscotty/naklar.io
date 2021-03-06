import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";

import { AccountRoutingModule } from "./account-routing.module";
import { TutorComponent } from "./tutor/tutor.component";
import { StudentComponent } from "./student/student.component";
import { TutorFormComponent } from "./tutor/tutor-form/tutor-form.component";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";

import { Ng5SliderModule } from "ng5-slider";
import { StudentFormComponent } from "./student/student-form/student-form.component";
import { LoginComponent } from "./login/login.component";
import { ProfileComponent } from "./profile/profile.component";
import { DatabaseService, AuthenticationService } from "../_services";

import { VerifyComponent } from "./verify/verify.component";

import { NgSelectModule } from "@ng-select/ng-select";
import { PasswordResetComponent } from "./password-reset/password-reset.component";
import { ResetRequestComponent } from "./password-reset/reset-request/reset-request.component";
import { MiscComponentsModule } from "../_misc_components/misc-components.module";
import { RegisterComponent } from "./register/register.component";
@NgModule({
  declarations: [
    TutorComponent,
    StudentComponent,
    TutorFormComponent,
    StudentFormComponent,
    LoginComponent,
    RegisterComponent,
    ProfileComponent,
    VerifyComponent,
    PasswordResetComponent,
    ResetRequestComponent,
  ],
  imports: [
    MiscComponentsModule,
    Ng5SliderModule,
    NgSelectModule,
    FormsModule,
    ReactiveFormsModule,
    CommonModule,
    AccountRoutingModule,
  ],
  providers: [DatabaseService, AuthenticationService],
})
export class AccountModule {}
