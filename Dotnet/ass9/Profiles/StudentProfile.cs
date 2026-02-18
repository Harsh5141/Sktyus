using AutoMapper;
using ass9.Models;
using ass9.DTOs;

namespace ass9.Profiles
{
    public class StudentProfile : Profile
    {
        public StudentProfile()
        {
            CreateMap<Student, StudentDTO>();
            CreateMap<CreateStudentDTO, Student>();
        }
    }
}
