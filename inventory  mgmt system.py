import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
# Database Setup
def setup_database():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            quantity INTEGER,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()
# User Authentication
def add_user(username, password):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
    finally:
        conn.close()
def authenticate_user(username, password):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user
# Inventory Management
def add_product(name, quantity, price):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))
    conn.commit()
    conn.close()
def edit_product(product_id, name, quantity, price):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET name=?, quantity=?, price=? WHERE id=?', (name, quantity, price, product_id))
    conn.commit()
    conn.close()
def delete_product(product_id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id=?', (product_id,))
    conn.commit()
    conn.close()
def get_products():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products
# GUI
class InventoryApp(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Inventory Management System")
        self.geometry("600x400")
        self.logged_in_user = None
        
        self.login_frame = tk.Frame(self)
        self.create_login_frame()
        
    def create_login_frame(self):
        tk.Label(self.login_frame, text="Username").grid(row=0, column=0)
        tk.Label(self.login_frame, text="Password").grid(row=1, column=0)
        
        self.username_entry = tk.Entry(self.login_frame)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        
        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)
        
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, columnspan=2)
        tk.Button(self.login_frame, text="Register", command=self.register).grid(row=3, columnspan=2)
        
        self.login_frame.pack(pady=20)
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = authenticate_user(username, password)
        if user:
            self.logged_in_user = user
            self.login_frame.pack_forget()
            self.create_inventory_frame()
        else:
            messagebox.showerror("Error", "Invalid username or password.")
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        add_user(username, password)
        messagebox.showinfo("Info", "Registration successful!")
    def create_inventory_frame(self):
        self.inventory_frame = tk.Frame(self)
        self.inventory_frame.pack(pady=20)
        self.product_name_entry = tk.Entry(self.inventory_frame)
        self.product_quantity_entry = tk.Entry(self.inventory_frame)
        self.product_price_entry = tk.Entry(self.inventory_frame)
        tk.Label(self.inventory_frame, text="Product Name").grid(row=0, column=0)
        tk.Label(self.inventory_frame, text="Quantity").grid(row=1, column=0)
        tk.Label(self.inventory_frame, text="Price").grid(row=2, column=0)
        self.product_name_entry.grid(row=0, column=1)
        self.product_quantity_entry.grid(row=1, column=1)
        self.product_price_entry.grid(row=2, column=1)
        tk.Button(self.inventory_frame, text="Add Product", command=self.add_product).grid(row=3, columnspan=2)
        tk.Button(self.inventory_frame, text="View Products", command=self.view_products).grid(row=4, columnspan=2)
    def add_product(self):
        name = self.product_name_entry.get()
        quantity = int(self.product_quantity_entry.get())
        price = float(self.product_price_entry.get())
        add_product(name, quantity, price)
        messagebox.showinfo("Info", "Product added!")
    def view_products(self):
        products = get_products()
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]}")
if __name__ == "__main__":
    setup_database()
    app = InventoryApp()
    app.mainloop()
add_product("Apples", 50, 0.50)
add_product("Bananas", 30, 0.30)
add_product("Bread", 20, 2.00)
add_product("Milk", 15, 1.50)
add_product("Eggs", 40, 0.10)
add_product("Chicken Breast", 25, 5.00)
add_product("Rice", 10, 1.20)
add_product("Cereal", 15, 3.50)

