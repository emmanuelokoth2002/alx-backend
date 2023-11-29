import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

// List of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Redis client setup
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);

// Function to get item by id
const getItemById = (id) => listProducts.find((item) => item.itemId === id);

// Function to reserve stock in Redis by item id
const reserveStockById = (itemId, stock) => {
  redisClient.set(`item.${itemId}`, stock);
};

// Async function to get the current reserved stock by item id
const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock, 10) : 0;
};

// Route to get the list of all products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map((item) => ({
    itemId: item.itemId,
    itemName: item.itemName,
    price: item.price,
    initialAvailableQuantity: item.initialAvailableQuantity,
  })));
});

// Route to get product details by item id
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (item) {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({
      itemId: item.itemId,
      itemName: item.itemName,
      price: item.price,
      initialAvailableQuantity: item.initialAvailableQuantity,
      currentQuantity: currentQuantity,
    });
  } else {
    res.json({ status: 'Product not found' });
  }
});

// Route to reserve product by item id
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);

  if (currentQuantity >= item.initialAvailableQuantity) {
    res.json({ status: 'Not enough stock available', itemId: itemId });
  } else {
    reserveStockById(itemId, currentQuantity + 1);
    res.json({ status: 'Reservation confirmed', itemId: itemId });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

export default app;
