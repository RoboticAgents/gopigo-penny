# Project 1: Building Ethical and Aggressive Robots

## Timeline

Activity                   | Deadline
-------------------------- | --------------------------------
Races:                     | September 15th, 2022 at 3pm
Part 2 Idea Due:           | September 15th, 2022 by midnight
Project Walkthrough:       | September 22nd, 2022 during lab
Demo and Final Submission: | September 27th, 2022 by 9:30am   |

## Class Community Guidelines

Throughout the completion of this project you must adhere to the [community guidelines](https://github.com/CMPSC-311-Allegheny-College-Fall-2022/course-information/blob/main/community_guidelines.md) that we developed as a class. To report any violations of the code of conduct, please submit an [anonymous form](https://forms.gle/tePfnLY12hyN1Xbd6). Students who think that the class should revise some aspect of the guidelines must use the GitHub issue tracker for that repository to suggest, discuss, and implement any required changes.

By working on and completing this assignment you agree to use the hardware given to you in a responsible manner. Each team is responsible for the safety and security of the robot while it is in your possession. You are allowed to take the robots used in this project outside of ALIC but you have to return all parts at the completion of this project, or if requested, at the end of the semester.

## Introduction

This project assignment invites you to work in a team to implement an ethical and/or aggressive robotic behavior while learning how to use `gopigo` robot and program it using Python programming language with a Raspberry Pi. This project consists of two portions. First, using the base `gopigo` robot, teams will participate in the robotic racing competitions during the next lab session. Secondly, teams will design a robotic application using `gopigo` for community demonstrations. Teams are also responsible for writing a detailed report, stored in the file `writing/report.md`. This is a Markdown file that must adhere to the standards described in the [Markdown Syntax Guide](https://guides.github.com/features/mastering-markdown/).

## Learning

To learn about ethical and aggressive robots please read an article titled [Why Ethical Robots Might Not Be Such a Good Idea After All](https://spectrum.ieee.org/automaton/robotics/artificial-intelligence/why-ethical-robots-might-not-be-such-a-good-idea-after-all) by Alan Winfield.

To learn about robotics ethics please refer to an article titled [Robot Ethics: Where Values and Engineering Meet](https://www.automate.org/blogs/robot-ethics-where-values-and-engineering-meet), which provides a lot of additional resources about this subject.

## Instructions

### 1\. Robotic Races

For the first portion of the project, we will hold robotic racing challenges during the beginning of the lab on Thursday, September 15th. You will need to build your robot and program it to be able to complete in a spring and box pushing races. You can elect to develop either an ethical (e.g., respectful) or an aggressive (e.g., interfering) robot behavior.

### Starting with the robot

- First, begin charging the battery, located in the little brown box.
- Then, it is time to start building your robot. Follow [gopigo's step-by-step instructions](https://gopigo.io/start).
- Once your robot is built, you can connect to the robot by following instructions for [pairing gopigo](https://gopigo.io/pairing-gopigo-os/).

  **Note:** When you are done using GoPiGo, turn off the robot first. Then, after the robot has shut down completely, turn off the rechargeable battery pack. If you turn off the battery before the robot, you run the risk of corrupting the microSD card.

- Finally, play around with your robot. Try to operate it via remote control. Then, begin experimenting with programs in Python.

### Race Rules

All robots will begin on the same line. The end line will be marked with tape. Robot positions (left/right) will be determined randomly by the instructor.

1. **Sprint race:** Robots will race along a straight path for three meters until the end line is reached. The robot that reaches the end line _first_ wins.
2. **Push race:** Each robot will have a small box right in front of it (front center). The robot needs to push the box along a straight path for three meters until it pushes the box across the end line. The robot that pushes the small box across the end line _first_ wins.

### 2\. Robot Design for Community Demonstrations

During the second portion of the project, each team will select a task for the robot to complete and then design and implement a `gopigo` robot to complete that task. This part of the project will be showcased during the community event this semester. Since there are no specific requirements or guidelines for this portion of the project, to ensure fairness in the amount of work you dedicate to this project, each team's selected task (what your robot will do) has to be approved by the instructor. In general, each team either needs to propose a unique robot design (e.g., the need to enhance the robot) and a solution for a simple task or a simple design (e.g., minimal need for robot restructuring) with a solution for a more complex task (e.g., involving multiple sensors). You can explore [project ideas at the gopigo](https://gopigo.io/projects/).

Additionally, since this part of the project will be used as an educational resource to get our local community (think, families with children) excited about computing, each team needs to develop concrete motivation for the educational purposes of your robotic design and development. Article on [Educational Robotics and Robot Creativity: An Interdisciplinary Dialogue](https://www.frontiersin.org/articles/10.3389/frobt.2021.662030/full) will give you some background into robotics used for education. Specifically, your project should have:

- Three learning objectives for the proposed demonstration.
- A hands-on component, which will either allow participants to experiment with the robot or observe varying performance of the robot under various scenarios.

You are required to finalize your idea by the end of the day (lab day) on September 15th and write about it in an appropriate subsection of the `report.md`'s "Planning for Robot Design for Community Demonstrations" section. Your team also needs to identify a timeline for completing this portion of the lab and include it in the table in the report. If you are in need of additional supplies that you could not find in ALIC, you need to include the list of supplies in the appropriate subsection of the report as well.

Instructor will review proposed project ideas and notify you of approval or alternate suggestions within 24 hours.

## Project Walkthrough

During the lab session on Thursday, September 22nd, each team will participate in the project walk-through process. Project walkthrough is an informal process where the instructor facilitates the process of reviewing the progress of the project and the written code. The purpose of this walkthrough is to motivate continuous progression on the project, identification of any conceptual issues, and detection of any technical errors. When the walkthrough is finished, the authors of the project are responsible for taking the necessary actions to correct the identified issues.

By this project walkthrough, each team should have identified the robot they plan to develop, and have implemented a significant portion of their intended solution. During the walkthrough, the team members will collaboratively lead the walkthrough process, which should last 5-10 minutes for each team. Each team should:

- Describe the chosen task.
- Explain and demonstrate the written code.
- Identify the steps left to complete for this project.

## Project Demonstration

At the beginning of the class session on Tuesday, September 27th, each team will be given an opportunity to demonstrate their project. When the lab session starts, teams will be given a few minutes to set up their demonstrations and get them running. Then, class members will participate in an interactive demonstration session, where everyone will be able to view each demonstration.

## Assignment Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 15%]:**: For lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes.

- **Mastery of Verbal Explanation during Walkthrough and Demonstration [up to 15%]:**: Since the continuous and timely project development and the ability to communicate technical details of a project is crucial to building successful software and hardware applications, a portion of students' lab grade will be determined based on the quality of the project walkthrough and the project demonstration.

- **Mastery of Technical Writing [up to 20%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `report.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 50%]**: Students will receive a portion of their assignment grade when their project implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this project. All programs must be inside `src/` directory. As a part of this grade, the instructor will assess aspects of the project including, but not limited to, the correctness of the program, the completeness and correctness of the software and hardware integration, the use of effective source code comments and Git commit messages.

All grades for this project will be reported through a student's gradebook GitHub repository (to be set up soon).

## GatorGrade

You can check the baseline writing and commit requirements of this project by running department's assignment checking `gatorgrade` tool To use `gatorgrade`, you first need to make sure you have Python installed. If not, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`:

`gatorgrade --config config/gatorgrade.yml`

## Assistance

If you are having trouble completing any part of this project, then please talk with the course instructor during the laboratory session. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.
