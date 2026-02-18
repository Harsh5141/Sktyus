using Microsoft.EntityFrameworkCore;
using ass9.Models;

namespace ass9.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options)
            : base(options) { }

        public DbSet<Student> Students { get; set; }
    }
}
