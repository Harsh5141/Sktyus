using System.ComponentModel.DataAnnotations;

namespace ass8.Models
{
    public class Student
    {
        public int Id { get; set; }

        [Required]
        public string Name { get; set; } = string.Empty;

        public string Department { get; set; } = string.Empty;

        public int Marks { get; set; }
    }
}
