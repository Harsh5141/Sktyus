using Microsoft.Extensions.Caching.Memory;

namespace ass13.Services
{
    public class ProductService
    {
        private readonly IMemoryCache _cache;
        private readonly ILogger<ProductService> _logger;

        public ProductService(IMemoryCache cache, ILogger<ProductService> logger)
        {
            _cache = cache;
            _logger = logger;
        }

        public List<string> GetProducts()
        {
            string cacheKey = "productList";

            if (!_cache.TryGetValue(cacheKey, out List<string>? products))
            {
                _logger.LogInformation("Fetching data from source...");

                // Simulate database delay
                Thread.Sleep(3000);

                products = new List<string>
                {
                    "Laptop",
                    "Mobile",
                    "Keyboard",
                    "Mouse"
                };

                var cacheOptions = new MemoryCacheEntryOptions()
                    .SetAbsoluteExpiration(TimeSpan.FromMinutes(5));

                _cache.Set(cacheKey, products, cacheOptions);
            }
            else
            {
                _logger.LogInformation("Fetching data from cache...");
            }

            return products!;
        }
    }
}