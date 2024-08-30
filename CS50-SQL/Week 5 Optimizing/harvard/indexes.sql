-- Create indexes for enrollments
CREATE INDEX "student_index_enrollment" ON "enrollments" ("student_id");
CREATE INDEX "course_index_enrollment" ON "enrollments" ("course_id");

-- Create Partial Index for the last 4 years in courses
CREATE INDEX "recents_courses" ON "courses" ("semester")
WHERE "semester" LIKE "%202_";

-- Create Index for Title in Courses
CREATE INDEX "course_title" ON "courses" ("title");
