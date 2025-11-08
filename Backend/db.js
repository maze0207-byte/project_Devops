// بيانات المنتجات (محاكاة قاعدة بيانات)
const products = [
  { id: 1, name: "Classic T-shirt", desc: "Comfortable cotton tee", img: "https://images.unsplash.com/photo-1521335629791-ce4aec67dd47?w=1200&q=60" },
  { id: 2, name: "Leather Jacket", desc: "Stylish and durable", img: "https://images.unsplash.com/photo-1593032465176-5e61435bdfd2?w=1200&q=60" },
  { id: 3, name: "Summer Dress", desc: "Light and breezy", img: "https://images.unsplash.com/photo-1602810312576-66f7b5d9b0b2?w=1200&q=60" }
];

const messages = []; // لتخزين رسائل المستخدمين

module.exports = { products, messages };
