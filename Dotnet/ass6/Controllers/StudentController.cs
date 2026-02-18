using Microsoft.AspNetCore.Mvc;
using CrudApp.Models;
using System.Collections.Generic;
using System.Linq;

namespace CrudApp.Controllers
{
    public class StudentController : Controller
    {
        private static List<Student> students = new List<Student>();
        private static int nextId = 1;

        // READ
        public IActionResult Index()
        {
            return View(students);
        }

        // CREATE - GET
        public IActionResult Create()
        {
            return View();
        }

        // CREATE - POST
        [HttpPost]
        public IActionResult Create(StudentViewModel model)
        {
            if (ModelState.IsValid)
            {
                var student = new Student
                {
                    Id = nextId++,
                    Name = model.Name,
                    Department = model.Department,
                    Marks = model.Marks
                };

                students.Add(student);
                return RedirectToAction("Index");
            }

            return View(model);
        }

        // EDIT - GET
        public IActionResult Edit(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student == null) return NotFound();

            var model = new StudentViewModel
            {
                Id = student.Id,
                Name = student.Name,
                Department = student.Department,
                Marks = student.Marks
            };

            return View(model);
        }

        // EDIT - POST
        [HttpPost]
        public IActionResult Edit(StudentViewModel model)
        {
            if (ModelState.IsValid)
            {
                var student = students.FirstOrDefault(s => s.Id == model.Id);
                if (student == null) return NotFound();

                student.Name = model.Name;
                student.Department = model.Department;
                student.Marks = model.Marks;

                return RedirectToAction("Index");
            }

            return View(model);
        }

        // DELETE
        public IActionResult Delete(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student != null)
                students.Remove(student);

            return RedirectToAction("Index");
        }
    }
}
