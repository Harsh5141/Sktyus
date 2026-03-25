using Microsoft.AspNetCore.Mvc;

namespace ass13.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class FileController : ControllerBase
    {
        private readonly IWebHostEnvironment _environment;
        private readonly ILogger<FileController> _logger;

        public FileController(IWebHostEnvironment environment, ILogger<FileController> logger)
        {
            _environment = environment;
            _logger = logger;
        }

        [HttpPost("upload")]
        public async Task<IActionResult> Upload(IFormFile file)
        {
            if (file == null || file.Length == 0)
            {
                _logger.LogWarning("Upload attempted with no file.");
                return BadRequest("No file uploaded.");
            }

            var uploadPath = Path.Combine(_environment.ContentRootPath, "Uploads");

            if (!Directory.Exists(uploadPath))
            {
                Directory.CreateDirectory(uploadPath);
            }

            var filePath = Path.Combine(uploadPath, file.FileName);

            using (var stream = new FileStream(filePath, FileMode.Create))
            {
                await file.CopyToAsync(stream);
            }

            _logger.LogInformation("File {FileName} uploaded successfully at {Time}", file.FileName, DateTime.UtcNow);

            return Ok(new
            {
                Message = "File uploaded successfully",
                FileName = file.FileName
            });
        }

        [HttpGet("download/{fileName}")]
public IActionResult Download(string fileName)
{
    var filePath = Path.Combine(_environment.ContentRootPath, "Uploads", fileName);

    if (!System.IO.File.Exists(filePath))
    {
        _logger.LogWarning("File {FileName} not found for download.", fileName);
        return NotFound("File not found.");
    }

    var bytes = System.IO.File.ReadAllBytes(filePath);

    _logger.LogInformation("File {FileName} downloaded at {Time}", fileName, DateTime.UtcNow);

    return File(bytes, "application/octet-stream", fileName);
}
    }
}

