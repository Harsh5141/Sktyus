using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;

namespace ass13.Filters
{
    public class GlobalExceptionFilter : IExceptionFilter
    {
        private readonly ILogger<GlobalExceptionFilter> _logger;

        public GlobalExceptionFilter(ILogger<GlobalExceptionFilter> logger)
        {
            _logger = logger;
        }

        public void OnException(ExceptionContext context)
        {
            _logger.LogError(context.Exception, "Exception caught in Global Filter");

            var response = new
            {
                StatusCode = 500,
                Message = "An error occurred in controller.",
                Detailed = context.Exception.Message
            };

            context.Result = new ObjectResult(response)
            {
                StatusCode = 500
            };

            context.ExceptionHandled = true;
        }
    }
}