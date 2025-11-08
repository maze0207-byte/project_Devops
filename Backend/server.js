const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
const PORT = 5000;
app.get('/', (req, res) => {
  res.send('Hello World');
});


app.use(cors());
app.use(bodyParser.json());

// Sample products
const products = [
  {id:1,name:"Red Dress",desc:"Elegant evening dress",img:"https://images.unsplash.com/photo-1618354691634-5db00ffed888?w=600"},
  {id:2,name:"Casual Shirt",desc:"Comfortable cotton shirt",img:"https://images.unsplash.com/photo-1520974735194-87b55f14b71f?w=600"},
  {id:3,name:"Blue Jeans",desc:"Stylish denim",img:"https://images.unsplash.com/photo-1618354829785-915bcab6c6d5?w=600"},
  {id:4,name:"Sneakers",desc:"Trendy sneakers for everyday",img:"https://images.unsplash.com/photo-1600180801572-b6a8e0f8b845?w=600"},
];

// GET products
app.get("/api/products", (req, res) => {
  res.json({success:true,products});
});

// POST contact
app.post("/api/contact", (req,res)=>{
  const {name,email,message} = req.body;
  console.log("New contact:",name,email,message);
  // هنا ممكن تضيف إرسال إيميل أو حفظ في قاعدة بيانات
  res.json({success:true});
});

app.listen(PORT, ()=>console.log(`Server running on http://localhost:${PORT}`));

