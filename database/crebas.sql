/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2023/10/18 14:13:40                          */
/*==============================================================*/


drop table if exists ChooseCourseMsg;

drop table if exists Course;

drop table if exists SignMsg;

drop table if exists Student;

drop table if exists Teacher;

drop table if exists signInMsg;

/*==============================================================*/
/* Table: ChooseCourseMsg                                       */
/*==============================================================*/
create table ChooseCourseMsg
(
   CourseID             char(10) not null,
   StudentID            char(15) not null,
   primary key (CourseID, StudentID)
);

/*==============================================================*/
/* Table: Course                                                */
/*==============================================================*/
create table Course
(
   CourseID             char(10) not null,
   TeacherNum           char(15) not null,
   ChooseNum            int not null,
   primary key (CourseID)
);

/*==============================================================*/
/* Table: SignMsg                                               */
/*==============================================================*/
create table SignMsg
(
   EachCourseID         char(10) not null,
   StudentID            char(15) not null,
   SignInWay            char(10) not null,
   primary key (StudentID)
);

/*==============================================================*/
/* Table: Student                                               */
/*==============================================================*/
create table Student
(
   StudentID            char(15) not null,
   Name                 char(10) not null,
   Colleage             char(10) not null,
   Class                char(10) not null,
   primary key (StudentID)
);

/*==============================================================*/
/* Table: Teacher                                               */
/*==============================================================*/
create table Teacher
(
   TeacherNum           char(15) not null,
   TeacherName          char(15) not null,
   Colleage             char(10) not null,
   primary key (TeacherNum)
);

/*==============================================================*/
/* Table: signInMsg                                             */
/*==============================================================*/
create table signInMsg
(
   CourseID             char(10) not null,
   EachCourseID         char(10) not null,
   SignInNum            int not null,
   BeginTime            date,
   primary key (EachCourseID)
);

alter table ChooseCourseMsg add constraint FK_Relationship_7 foreign key (StudentID)
      references Student (StudentID) on delete restrict on update restrict;

alter table ChooseCourseMsg add constraint FK_Relationship_8 foreign key (CourseID)
      references Course (CourseID) on delete restrict on update restrict;

alter table Course add constraint FK_Relationship_1 foreign key (TeacherNum)
      references Teacher (TeacherNum) on delete restrict on update restrict;

alter table SignMsg add constraint FK_Relationship_4 foreign key (StudentID)
      references Student (StudentID) on delete restrict on update restrict;

alter table SignMsg add constraint FK_Relationship_5 foreign key (EachCourseID)
      references signInMsg (EachCourseID) on delete restrict on update restrict;

alter table signInMsg add constraint FK_Relationship_2 foreign key (CourseID)
      references Course (CourseID) on delete restrict on update restrict;

