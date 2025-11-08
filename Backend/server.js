const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const { products, messages } = require("./db");

const app = express();
app.use(cors());
app.use(bodyParser.json());

// جلب المنتجات
app.get("/api/products", (req, res) => {
  res.json(products);
});

// إرسال رسالة تواصل
app.post("/api/contact", (req, res) => {
  const { name, email, message } = req.body;
  if(name && email && message){
    messages.push({ name, email, message });
    res.json({ success: true });
  } else {
    res.json({ success: false });
  }
});

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
