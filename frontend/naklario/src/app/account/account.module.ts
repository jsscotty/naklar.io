import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";

import { AccountRoutingModule } from "./account-routing.module";
import { TutorComponent } from "./tutor/tutor.component";
import { StudentComponent } from "./student/student.component";
import { TutorRegisterComponent } from "./tutor/tutor-register/tutor-register.component";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";

import { Ng5SliderModule } from "ng5-slider";
import { StudentRegisterComponent } from "./student/student-register/student-register.component";
import { TermsConditionsComponent, ImgUploadComponent } from "../_misc_components";
import { LoginComponent } from "./login/login.component";
import { ProfileComponent } from "./profile/profile.component";

@NgModule({
  declarations: [
    TutorComponent,
    StudentComponent,
    TutorRegisterComponent,
    ImgUploadComponent,
    StudentRegisterComponent,
    TermsConditionsComponent,
    LoginComponent,
    ProfileComponent,
  ],
  imports: [
    Ng5SliderModule,
    FormsModule,
    ReactiveFormsModule,
    CommonModule,
    AccountRoutingModule,
  ],
})
export class AccountModule {}