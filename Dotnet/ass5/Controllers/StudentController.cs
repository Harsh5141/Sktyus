using Microsoft.AspNetCore.Mvc;
using MvcDemoApp.Models;
using System.Collections.Generic;

namespace MvcDemoApp.Controllers
{
    public class StudentController : Controller
    {
        public IActionResult Index()
        {
            var students = new List<Student>
            {
                new Student { Id = 1, Name = "Harsh", Department = "Computer", Marks = 85 },
                new Student { Id = 2, Name = "Riya", Department = "IT", Marks = 92 },
                new Student { Id = 3, Name = "Amit", Department = "Mechanical", Marks = 70 }
            };

            return View(students);
        }
    }
}
