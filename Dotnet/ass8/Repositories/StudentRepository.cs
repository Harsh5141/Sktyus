using ass8.Data;
using ass8.Models;

namespace ass8.Repositories
{
    public class StudentRepository : IStudentRepository
    {
        private readonly AppDbContext _context;

        public StudentRepository(AppDbContext context)
        {
            _context = context;
        }

        public IEnumerable<Student> GetAll()
        {
            return _context.Students
                           .OrderBy(s => s.Name)
                           .ToList();
        }

        public Student? GetById(int id)
        {
            return _context.Students
                           .FirstOrDefault(s => s.Id == id);
        }

        public void Add(Student student)
        {
            _context.Students.Add(student);
        }

        public void Update(Student student)
        {
            _context.Students.Update(student);
        }

        public void Delete(int id)
        {
            var student = _context.Students
                                  .FirstOrDefault(s => s.Id == id);

            if (student != null)
                _context.Students.Remove(student);
        }

        public void Save()
        {
            _context.SaveChanges();
        }
    }
}
