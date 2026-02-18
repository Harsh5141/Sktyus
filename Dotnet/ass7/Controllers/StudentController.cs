using Microsoft.AspNetCore.Mvc;
using ass7.Data;
using ass7.Models;
using System.Linq;

namespace ass7.Controllers
{
    public class StudentController : Controller
    {
        private readonly ApplicationDbContext _context;

        public StudentController(ApplicationDbContext context)
        {
            _context = context;
        }

        // LIST
        public IActionResult Index()
        {
            var students = _context.Students.ToList();
            return View(students);
        }

        // SEED DATA
        public IActionResult Seed()
        {
            if (!_context.Students.Any())
            {
                _context.Students.AddRange(
                    new Student { Name = "Harsh", Department = "Computer", Marks = 90 },
                    new Student { Name = "Riya", Department = "IT", Marks = 85 },
                    new Student { Name = "Amit", Department = "Mechanical", Marks = 70 }
                );

                _context.SaveChanges();
            }

            return RedirectToAction("Index");
        }
    }
}
