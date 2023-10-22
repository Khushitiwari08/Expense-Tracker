import tkinter as tk
import sqlite3

class InventoryManagementSystem:
    def __init__(self, master):
        self.master = master
        master.title("Inventory Management System")
        
        # Create a database connection and cursor
        self.conn = sqlite3.connect('inventory.db')
        self.c = self.conn.cursor()
        
        # Create inventory table if it doesn't exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS inventory
            (id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            quantity INTEGER,
            price REAL)''')
        
        # Create GUI elements
        self.inventory_label = tk.Label(master, text="Inventory")
        self.inventory_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.inventory_listbox = tk.Listbox(master, width=50)
        self.inventory_listbox.grid(row=1, column=0, padx=10, pady=10)
        
        self.refresh_button = tk.Button(master, text="Refresh", command=self.refresh_inventory)
        self.refresh_button.grid(row=2, column=0, padx=10, pady=10)
        
        self.add_button = tk.Button(master, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)
        
        # Populate inventory listbox
        self.refresh_inventory()
    
    def refresh_inventory(self):
        # Clear inventory listbox
        self.inventory_listbox.delete(0, tk.END)
        
        # Get inventory data from database
        self.c.execute("SELECT * FROM inventory")
        inventory_data = self.c.fetchall()
        
        # Add inventory data to listbox
        for item in inventory_data:
            self.inventory_listbox.insert(tk.END, f"{item[1]} ({item[2]}): {item[3]} x {item[4]}")
    
    def add_item(self):
        # Create a new window for adding an item
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Add Item")
        
        # Create GUI elements for add window
        tk.Label(self.add_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.add_window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.add_window, text="Category:").grid(row=1, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(self.add_window)
        self.category_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.add_window, text="Quantity:").grid(row=2, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(self.add_window)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self.add_window, text="Price:").grid(row=3, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(self.add_window)
        self.price_entry.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Button(self.add_window, text="Add Item", command=self.save_item).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    