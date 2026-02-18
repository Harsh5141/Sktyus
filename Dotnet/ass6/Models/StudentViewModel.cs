using System.ComponentModel.DataAnnotations;

namespace CrudApp.Models
{
    public class StudentViewModel
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "Enter student name")]
        public string Name { get; set; }

        [Required(ErrorMessage = "Enter department")]
        public string Department { get; set; }

        [Range(0,100, ErrorMessage = "Marks must be between 0 and 100")]
        public int Marks { get; set; }
    }
}
