import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";

import { NgbModule } from "@ng-bootstrap/ng-bootstrap";

import { UserCardComponent } from "./user-card/user-card.component";
import { ToastsComponent } from "./toasts/toasts.component";
import { ImgUploadComponent } from "./img-upload/img-upload.component";

import { StudentExplanationComponent } from "./student-explanation/student-explanation.component";
import { TutorExplanationComponent } from "./tutor-explanation/tutor-explanation.component";
import { SafePipe } from "./safe.pipe";
import { CloseModalDirective } from "./closeModal.directive";
import { AudioAutoplayComponent } from "./audio-autoplay/audio-autoplay.component";

@NgModule({
  declarations: [
    ImgUploadComponent,
    ToastsComponent,
    UserCardComponent,
    SafePipe,
    StudentExplanationComponent,
    TutorExplanationComponent,
    AudioAutoplayComponent,
    CloseModalDirective,
  ],
  imports: [CommonModule, NgbModule],
  exports: [
    ImgUploadComponent,
    ToastsComponent,
    UserCardComponent,
    SafePipe,
    StudentExplanationComponent,
    TutorExplanationComponent,
    AudioAutoplayComponent,
    CloseModalDirective,
  ],
})
export class MiscComponentsModule {}
