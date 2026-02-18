using System;
using System.Collections.Generic;
using System.Linq;

namespace StudentApp
{
    class Student
    {
        // 🔹 Properties (Encapsulation using get/set)
        public int StudentId { get; set; }
        public string Name { get; set; }
        public string Department { get; set; }
        public int Year { get; set; }
        public int Marks { get; set; }

        // 🔹 Constructor
        public Student(int studentId, string name, string department, int year, int marks)
        {
            StudentId = studentId;
            Name = name;
            Department = department;
            Year = year;
            Marks = marks;
        }

        // 🔹 Method to display student info
        public void Display()
        {
            Console.WriteLine($"ID: {StudentId}, Name: {Name}, Dept: {Department}, Year: {Year}, Marks: {Marks}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // 🔹 Creating Multiple Student Objects
            List<Student> students = new List<Student>()
            {
                new Student(1, "Harsh", "Computer", 2, 82),
                new Student(2, "Riya", "IT", 3, 91),
                new Student(3, "Amit", "Mechanical", 1, 68),
                new Student(4, "Neha", "Computer", 4, 76),
                new Student(5, "Kunal", "Civil", 2, 88),
                new Student(6, "Priya", "IT", 3, 95)
            };

            Console.WriteLine("===== ALL STUDENTS =====");
            foreach (var student in students)
            {
                student.Display();
            }

            // 🔹 Students with Marks > 75
            Console.WriteLine("\n===== STUDENTS WITH MARKS > 75 =====");
            var highScorers = students.Where(s => s.Marks > 75);
            foreach (var student in highScorers)
            {
                student.Display();
            }

            // 🔹 Sort Students by Marks (Descending)
            Console.WriteLine("\n===== SORTED BY MARKS (HIGH TO LOW) =====");
            var sortedStudents = students.OrderByDescending(s => s.Marks);
            foreach (var student in sortedStudents)
            {
                student.Display();
            }

            // 🔹 Top 3 Scorers
            Console.WriteLine("\n===== TOP 3 SCORERS =====");
            var top3 = students.OrderByDescending(s => s.Marks).Take(3);
            foreach (var student in top3)
            {
                student.Display();
            }
        }
    }
}
