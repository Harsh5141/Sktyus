using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;
using ass4.Services;


public class HomeController : Controller
{
    private readonly IConfiguration _configuration;
    private readonly IMyService _myService;
    private readonly ILogger<HomeController> _logger;

    public HomeController(
        IConfiguration configuration,
        IMyService myService,
        ILogger<HomeController> logger)
    {
        _configuration = configuration;
        _myService = myService;
        _logger = logger;
    }

    public IActionResult Index()
    {
        var appName = _configuration["MySettings:AppName"];
        var version = _configuration["MySettings:Version"];
        var serviceMessage = _myService.GetWelcomeMessage();

        _logger.LogInformation("Home page accessed");

        ViewBag.Message = $"{appName} - {version}";
        ViewBag.ServiceMessage = serviceMessage;

        return View();
    }
}
