from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os


# =========================================================
# FLASK APPLICATION
# =========================================================

app = Flask(__name__)


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = None

if API_KEY and API_KEY != "your_new_api_key_here":
    client = OpenAI(api_key=API_KEY)


MODEL = "gpt-5.6-luna"


# =========================================================
# LOCAL DEMO ANSWERS
# =========================================================

def local_answer(question, mode):

    q = question.lower().strip()

    # -----------------------------------------------------
    # POLYMORPHISM
    # -----------------------------------------------------

    if "polymorphism" in q and "java" in q:

        return """
JAVA POLYMORPHISM
=================

Definition:
Polymorphism means "many forms".

In Java, polymorphism allows the same method
name to perform different actions.

Types of Polymorphism:

1. Compile-time Polymorphism
   - Achieved using method overloading.

2. Runtime Polymorphism
   - Achieved using method overriding.


Example:

class Animal {

    void sound() {
        System.out.println("Animal makes sound");
    }
}

class Dog extends Animal {

    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

public class Main {

    public static void main(String[] args) {

        Animal a = new Dog();

        a.sound();
    }
}


Output:

Dog barks


Advantages:

1. Code flexibility
2. Code reusability
3. Easy maintenance
4. Supports method overriding


Exam Point:

Polymorphism allows one method or interface
to have multiple forms.
"""


    # -----------------------------------------------------
    # INHERITANCE
    # -----------------------------------------------------

    if "inheritance" in q and "java" in q:

        return """
JAVA INHERITANCE
================

Definition:

Inheritance is a feature of Java where one
class acquires the properties and methods
of another class.

The existing class is called the parent class.

The new class is called the child class.


Example:

class Animal {

    void eat() {
        System.out.println("Animal eats");
    }
}

class Dog extends Animal {

    void bark() {
        System.out.println("Dog barks");
    }
}


Here Dog inherits the eat() method from Animal.


Advantages:

1. Code reusability
2. Easy maintenance
3. Method overriding
4. Reduces duplicate code
"""


    # -----------------------------------------------------
    # ENCAPSULATION
    # -----------------------------------------------------

    if "encapsulation" in q and "java" in q:

        return """
JAVA ENCAPSULATION
==================

Definition:

Encapsulation means wrapping data and methods
together inside a class.

It also protects data from direct access.


Example:

class Student {

    private int marks;

    public void setMarks(int marks) {
        this.marks = marks;
    }

    public int getMarks() {
        return marks;
    }
}


Advantages:

1. Data security
2. Controlled access
3. Better organization
4. Easy maintenance


Exam Point:

Encapsulation is mainly achieved using
private variables and public getter/setter methods.
"""


    # -----------------------------------------------------
    # ABSTRACTION
    # -----------------------------------------------------

    if "abstraction" in q and "java" in q:

        return """
JAVA ABSTRACTION
================

Definition:

Abstraction means hiding implementation
details and showing only the important
features of an object.

Java achieves abstraction using:

1. Abstract classes
2. Interfaces


Example:

abstract class Animal {

    abstract void sound();

    void eat() {
        System.out.println("Animal eats");
    }
}

class Dog extends Animal {

    void sound() {
        System.out.println("Dog barks");
    }
}


Advantages:

1. Hides implementation details
2. Reduces complexity
3. Improves security
4. Improves program structure
"""


    # -----------------------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------------------

    if "constructor" in q and "java" in q:

        return """
JAVA CONSTRUCTOR
================

Definition:

A constructor is a special member used
to initialize objects in Java.

Important Points:

1. Constructor name is the same as the class name.
2. Constructor does not have a return type.
3. Constructor is automatically called when
   an object is created.


Example:

class Student {

    Student() {
        System.out.println("Constructor called");
    }
}


public class Main {

    public static void main(String[] args) {

        Student s = new Student();

    }
}


Output:

Constructor called
"""


    # -----------------------------------------------------
    # INTERFACE
    # -----------------------------------------------------

    if "interface" in q and "java" in q:

        return """
JAVA INTERFACE
==============

Definition:

An interface is a contract that specifies
methods that a class must implement.

Interfaces are commonly used for abstraction
and multiple inheritance of type.


Example:

interface Animal {

    void sound();

}


class Dog implements Animal {

    public void sound() {

        System.out.println("Dog barks");

    }
}


Here Dog implements the Animal interface.


Advantages:

1. Abstraction
2. Loose coupling
3. Multiple inheritance of type
4. Better program structure
"""


    # -----------------------------------------------------
    # JAVA
    # -----------------------------------------------------

    if "java" in q:

        return """
JAVA PROGRAMMING
================

Java is a high-level, object-oriented
programming language.

Important features:

1. Object-oriented
2. Platform independent
3. Secure
4. Robust
5. Portable
6. Multithreaded


Example:

public class Main {

    public static void main(String[] args) {

        System.out.println("Hello World");

    }
}


Output:

Hello World
"""


    # -----------------------------------------------------
    # PYTHON
    # -----------------------------------------------------

    if "python" in q:

        return """
PYTHON
======

Python is a high-level, interpreted
programming language.

Features:

1. Easy to learn
2. Simple syntax
3. Object-oriented
4. Large library support
5. Used in AI
6. Used in Machine Learning
7. Used in Web Development


Example:

print("Hello World")


Output:

Hello World
"""


    # -----------------------------------------------------
    # CPU
    # -----------------------------------------------------

    if "cpu" in q:

        return """
CPU
===

CPU stands for Central Processing Unit.

It is commonly called the brain of
the computer.


Functions:

1. Executes instructions
2. Performs calculations
3. Processes data
4. Controls computer operations


Example:

When you open an application,
the CPU processes the instructions
required to run that application.
"""


    # -----------------------------------------------------
    # RAM
    # -----------------------------------------------------

    if "ram" in q:

        return """
RAM
===

RAM stands for Random Access Memory.

It temporarily stores data and programs
that are currently being used.

RAM is volatile memory.

This means data is normally lost when
the computer is turned off.


Example:

When you open Google Chrome,
Chrome uses RAM while it is running.
"""


    # -----------------------------------------------------
    # OPERATING SYSTEM
    # -----------------------------------------------------

    if "operating system" in q or q == "os":

        return """
OPERATING SYSTEM
================

An Operating System is system software
that manages computer hardware and software.


Examples:

• Windows
• Linux
• macOS
• Android
• iOS


Functions:

1. Memory management
2. Process management
3. File management
4. Device management
5. Security
6. User interface
"""


    # -----------------------------------------------------
    # HTML
    # -----------------------------------------------------

    if "html" in q:

        return """
HTML
====

HTML stands for HyperText Markup Language.

It is used to create the structure
of web pages.


Example:

<!DOCTYPE html>

<html>

<body>

<h1>Hello World</h1>

</body>

</html>


HTML is a markup language rather than
a programming language.
"""


    # -----------------------------------------------------
    # CSS
    # -----------------------------------------------------

    if "css" in q:

        return """
CSS
===

CSS stands for Cascading Style Sheets.

It is used to design and style web pages.


CSS can control:

• Colors
• Fonts
• Backgrounds
• Spacing
• Layout
• Animations


Example:

body {

    background-color: blue;

    color: white;

}
"""


    # -----------------------------------------------------
    # ATTENDANCE
    # -----------------------------------------------------

    if "attendance" in q:

        return """
COLLEGE FAQ - ATTENDANCE
========================

Attendance requirements depend on your
college and university rules.

You should check:

• College attendance policy
• Department notice
• Student handbook
• Faculty instructions


StudyAI does not invent college-specific
attendance rules.
"""


    # -----------------------------------------------------
    # EXAM
    # -----------------------------------------------------

    if "exam" in q:

        return """
COLLEGE FAQ - EXAMS
===================

For exam preparation:

1. Check your syllabus.
2. Study important definitions.
3. Practice previous questions.
4. Prepare short notes.
5. Practice programming problems.
6. Revise before the examination.


Tip:

Study one topic at a time instead of
trying to learn everything together.
"""


    # -----------------------------------------------------
    # ASSIGNMENT
    # -----------------------------------------------------

    if "assignment" in q:

        return """
COLLEGE FAQ - ASSIGNMENTS
=========================

For an assignment:

1. Read the question carefully.
2. Understand the requirements.
3. Prepare the solution.
4. Test your work.
5. Add screenshots if required.
6. Check formatting.
7. Submit before the deadline.
"""


    # -----------------------------------------------------
    # PROJECT
    # -----------------------------------------------------

    if "project" in q:

        return """
COLLEGE FAQ - PROJECT
=====================

A college project normally contains:

1. Project title
2. Introduction
3. Problem statement
4. Objectives
5. Technologies used
6. System design
7. Implementation
8. Testing
9. Results
10. Conclusion


For a software project, keep your
folder structure organized.
"""


    # -----------------------------------------------------
    # DEFAULT
    # -----------------------------------------------------

    return f"""
STUDY ASSISTANT
===============

Your Question:

{question}


Selected Mode:

{mode.upper()}


LOCAL DEMO MODE

The AI service is currently unavailable,
so StudyAI is using its built-in demo
knowledge.

Try questions such as:

• Explain polymorphism in Java
• Explain inheritance in Java
• What is encapsulation in Java?
• What is abstraction?
• What is a Java constructor?
• What is a Java interface?
• What is Python?
• What is CPU?
• What is RAM?
• What is HTML?
• What is CSS?
• What is an operating system?
• How should I prepare for exams?
• How can I complete my project?
"""


# =========================================================
# PROMPT GENERATOR
# =========================================================

def create_prompt(question, mode):

    if mode == "zero":

        return f"""
You are StudyAI, a college study assistant.

Answer the student's question directly.

Use simple beginner-friendly language.

Structure the answer using:

1. Definition
2. Explanation
3. Example
4. Important exam points

If the question requires code, provide a
small correct code example.

Student question:

{question}
"""


    elif mode == "few":

        return f"""
You are StudyAI, a college study assistant.

Use example-based teaching.

First understand the concept, then explain
the student's question using simple examples.

Answer with:

1. Simple explanation
2. Example
3. Code example if appropriate
4. Exam points

Avoid unnecessary complicated terminology.

Student question:

{question}
"""


    elif mode == "role":

        return f"""
You are an experienced college teacher.

Teach the following question to a beginner.

Explain step by step.

Include:

1. Basic concept
2. Detailed explanation
3. Real-world example
4. Programming example if applicable
5. Important exam points
6. Short revision summary

Use clear and student-friendly language.

Student question:

{question}
"""


    elif mode == "faq":

        return f"""
You are StudyAI College FAQ Assistant.

The student is asking a college-related
question.

Answer clearly and practically.

Possible topics include:

• Exams
• Assignments
• Projects
• Attendance
• Classes
• Laboratory work
• Programming
• Study preparation

Do not invent specific college policies,
dates, fees, attendance percentages, or
rules.

If a question depends on the student's
college, tell the student to check the
official college notice, handbook, or
faculty instructions.

Student question:

{question}
"""


    return create_prompt(question, "zero")


# =========================================================
# OPENAI ANSWER
# =========================================================

def openai_answer(question, mode):

    # No API key
    if client is None:

        return local_answer(
            question,
            mode
        ), "demo"

    prompt = create_prompt(
        question,
        mode
    )

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    answer = response.output_text

    if not answer:

        return local_answer(
            question,
            mode
        ), "demo"

    return answer, "ai"


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""
    question = ""
    selected_mode = "zero"
    answer_source = ""

    if request.method == "POST":

        question = request.form.get(
            "question",
            ""
        ).strip()

        selected_mode = request.form.get(
            "mode",
            "zero"
        ).strip()

        allowed_modes = {
            "zero",
            "few",
            "role",
            "faq"
        }

        if selected_mode not in allowed_modes:
            selected_mode = "zero"

        # Empty question
        if not question:

            answer = "Please enter a question."

            answer_source = "error"

        # Question too long
        elif len(question) > 5000:

            answer = """
Your question is too long.

Please keep the question below 5000 characters.
"""

            answer_source = "error"

        else:

            try:

                answer, answer_source = openai_answer(
                    question,
                    selected_mode
                )

            except Exception as e:

                error_text = str(e).lower()

                # API quota / rate limit / credit
                if (
                    "429" in error_text
                    or "quota" in error_text
                    or "insufficient" in error_text
                    or "rate limit" in error_text
                    or "credit" in error_text
                ):

                    answer = local_answer(
                        question,
                        selected_mode
                    )

                    answer_source = "demo"

                else:

                    answer = """
The AI service could not answer right now.

StudyAI has switched to Demo Mode.

Please check:

1. Your API key
2. Your internet connection
3. Your OpenAI API access
4. Your API billing/quota
"""

                    answer_source = "error"


    # API status
    if client is not None:

        api_status = "AI Ready"

    else:

        api_status = "Demo Mode"


    return render_template(
        "index.html",
        answer=answer,
        question=question,
        selected_mode=selected_mode,
        answer_source=answer_source,
        api_status=api_status
    )


# =========================================================
# HEALTH CHECK
# =========================================================

@app.route("/health")
def health():

    return {
        "application": "StudyAI",
        "status": "running",
        "ai_configured": client is not None,
        "model": MODEL
    }


# =========================================================
# RUN SERVER
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
