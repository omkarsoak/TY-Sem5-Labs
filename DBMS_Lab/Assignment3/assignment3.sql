USE UNIVERSITY;
CREATE TABLE IF NOT EXISTS TEACHING_ASSISTANT(	
	ID			varchar(5), 
	course_id		varchar(8),
	sec_id			varchar(8), 
	semester		varchar(6),
	year			numeric(4,0),
	primary key (ID, course_id, sec_id, semester, year),
	foreign key (course_id,sec_id, semester, year) references section(course_id,sec_id, semester, year) on delete cascade
 );
 
-- To remove foreign key constraints.
ALTER TABLE advisor DROP constraint advisor_ibfk_1;
ALTER TABLE advisor DROP constraint advisor_ibfk_2;

-- To drop primary key
ALTER TABLE advisor DROP primary key;

-- to add multiple primary keys and add foreign key constraints
ALTER TABLE advisor ADD PRIMARY key (s_ID,i_ID);
ALTER TABLE advisor ADD foreign key (i_ID) references instructor (ID), 
ADD foreign key (s_ID) references student (ID) on delete cascade;

-- inserting new dvalues (contains mutiple advisors)
INSERT INTO advisor (s_ID, i_ID) VALUES ('23121', '76766');
INSERT INTO advisor (s_ID, i_ID) VALUES ('23121', '45565');
INSERT INTO advisor (s_ID, i_ID) VALUES ('54321', '22222');
INSERT INTO advisor (s_ID, i_ID) VALUES ('54321', '76766');
INSERT INTO advisor (s_ID, i_ID) VALUES ('54321', '45565');

SELECT s_ID FROM advisor GROUP BY s_ID HAVING COUNT(i_ID) >= 3;

SELECT s_ID FROM advisor WHERE i_ID IN 
(SELECT ID FROM instructor WHERE name IN ('Srinivasan', 'Ashok')) GROUP BY s_ID;

SELECT a.s_ID FROM advisor a JOIN instructor i ON a.i_ID = i.ID 
GROUP BY a.s_ID HAVING COUNT(DISTINCT i.dept_name) > 1;

DELETE FROM takes WHERE year < (EXTRACT(YEAR FROM CURRENT_DATE) - 10);
DELETE FROM teaches WHERE year < (EXTRACT(YEAR FROM CURRENT_DATE) - 10);
DELETE FROM section WHERE year < (EXTRACT(YEAR FROM CURRENT_DATE) - 10);

ALTER TABLE prereq ADD CONSTRAINT fk_prereq_course 
FOREIGN KEY (prereq_id) REFERENCES course(course_id) ON DELETE CASCADE;

DELETE FROM course WHERE course_id = 'CS-101';

select * from prereq;
