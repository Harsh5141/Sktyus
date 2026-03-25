using Microsoft.AspNetCore.Mvc;

namespace ass13.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TestController : ControllerBase
    {
        private readonly ILogger<TestController> _logger;

        public TestController(ILogger<TestController> logger)
        {
            _logger = logger;
        }

        [HttpGet("success")]
        public IActionResult Success()
        {
            _logger.LogInformation("Success endpoint called at {Time}", DateTime.UtcNow);
            return Ok("Success logged");
        }

        [HttpGet("warning")]
        public IActionResult Warning()
        {
            _logger.LogWarning("Warning triggered at {Time}", DateTime.UtcNow);
            return Ok("Warning logged");
        }

        [HttpGet("error")]
        public IActionResult Error()
        {
            _logger.LogError("Manual error log at {Time}", DateTime.UtcNow);
            throw new Exception("Manual exception for testing");
        }
    }
}