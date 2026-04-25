import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Currency Converter")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        
        # API configuration
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.exchange_rates = {}
        self.last_updated = ""
        
        # Common currencies
        self.currencies = [
            "USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "CNY", 
            "CHF", "SGD", "HKD", "NZD", "KRW", "BRL", "ZAR", "MXN"
        ]
        
        # Fetch initial rates
        self.fetch_exchange_rates()
        
        # Setup GUI
        self.setup_gui()
        
    def fetch_exchange_rates(self):
        """Fetch live exchange rates from API"""
        try:
            response = requests.get(self.api_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.exchange_rates = data['rates']
                self.last_updated = data['date']
                return True
            else:
                messagebox.showerror("Error", "Failed to fetch exchange rates!\nUsing fallback rates.")
                self.set_fallback_rates()
                return False
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No internet connection!\nUsing fallback rates.")
            self.set_fallback_rates()
            return False
    
    def set_fallback_rates(self):
        """Fallback rates if API fails"""
        self.exchange_rates = {
            "USD": 1.0, "EUR": 0.92, "GBP": 0.79, "INR": 83.5, 
            "JPY": 151.2, "CAD": 1.36, "AUD": 1.52, "CNY": 7.24,
            "CHF": 0.91, "SGD": 1.35, "HKD": 7.82, "NZD": 1.66,
            "KRW": 1350.5, "BRL": 5.12, "ZAR": 18.95, "MXN": 17.03
        }
        self.last_updated = "2024-01-01 (Fallback)"
    
    def setup_gui(self):
        """Setup all GUI elements"""
        
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="💱 Currency Converter", 
                               font=("Arial", 20, "bold"), 
                               fg="white", bg="#2c3e50")
        title_label.pack(pady=20)
        
        # Main Frame
        main_frame = tk.Frame(self.root, bg="#ecf0f1", padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Amount Input
        tk.Label(main_frame, text="Amount:", font=("Arial", 12), 
                bg="#ecf0f1").grid(row=0, column=0, sticky="w", pady=(0,5))
        
        self.amount_entry = tk.Entry(main_frame, font=("Arial", 14), 
                                     width=20, relief="solid", bd=1)
        self.amount_entry.grid(row=1, column=0, columnspan=2, pady=(0,15), sticky="ew")
        self.amount_entry.insert(0, "1")
        
        # From Currency
        tk.Label(main_frame, text="From Currency:", font=("Arial", 12), 
                bg="#ecf0f1").grid(row=2, column=0, sticky="w", pady=(0,5))
        
        self.from_currency = ttk.Combobox(main_frame, values=self.currencies, 
                                          font=("Arial", 12), width=18)
        self.from_currency.grid(row=3, column=0, pady=(0,15), padx=(0,10))
        self.from_currency.set("USD")
        
        # Swap Button
        swap_btn = tk.Button(main_frame, text="⇄", font=("Arial", 16), 
                            bg="#3498db", fg="white", width=4,
                            command=self.swap_currencies)
        swap_btn.grid(row=3, column=1, pady=(0,15))
        
        # To Currency
        tk.Label(main_frame, text="To Currency:", font=("Arial", 12), 
                bg="#ecf0f1").grid(row=4, column=0, sticky="w", pady=(0,5))
        
        self.to_currency = ttk.Combobox(main_frame, values=self.currencies, 
                                        font=("Arial", 12), width=18)
        self.to_currency.grid(row=5, column=0, pady=(0,20))
        self.to_currency.set("EUR")
        
        # Convert Button
        convert_btn = tk.Button(main_frame, text="🔄 Convert", font=("Arial", 14, "bold"),
                               bg="#27ae60", fg="white", height=2,
                               command=self.convert_currency)
        convert_btn.grid(row=6, column=0, columnspan=2, pady=(0,20), sticky="ew")
        
        # Result Frame
        result_frame = tk.Frame(main_frame, bg="white", relief="solid", bd=1)
        result_frame.grid(row=7, column=0, columnspan=2, pady=(0,10), sticky="ew")
        result_frame.grid_columnconfigure(0, weight=1)
        
        self.result_label = tk.Label(result_frame, text="", font=("Arial", 16, "bold"),
                                    bg="white", fg="#2c3e50", pady=20)
        self.result_label.pack()
        
        # Rate Info
        self.rate_label = tk.Label(main_frame, text="", font=("Arial", 9),
                                  bg="#ecf0f1", fg="#7f8c8d")
        self.rate_label.grid(row=8, column=0, columnspan=2)
        
        # Update Button
        update_btn = tk.Button(main_frame, text="Update Rates", font=("Arial", 10),
                              bg="#95a5a6", fg="white", command=self.refresh_rates)
        update_btn.grid(row=9, column=0, columnspan=2, pady=(10,0))
        
        # Show last update time
        self.update_time_label = tk.Label(main_frame, text="", font=("Arial", 8),
                                         bg="#ecf0f1", fg="#95a5a6")
        self.update_time_label.grid(row=10, column=0, columnspan=2, pady=(5,0))
        self.update_time_label.config(text=f"Last updated: {self.last_updated}")
        
        # Configure grid weights
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=0)
        
    def convert_currency(self):
        """Perform currency conversion"""
        try:
            # Get amount
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showwarning("Warning", "Please enter a positive amount!")
                return
            
            # Get currencies
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            # Validate currencies
            if from_curr not in self.exchange_rates or to_curr not in self.exchange_rates:
                messagebox.showerror("Error", "Invalid currency selected!")
                return
            
            # Convert
            usd_amount = amount / self.exchange_rates[from_curr]
            converted_amount = usd_amount * self.exchange_rates[to_curr]
            
            # Display result
            result_text = f"{amount:,.2f} {from_curr} = {converted_amount:,.2f} {to_curr}"
            self.result_label.config(text=result_text)
            
            # Display exchange rate
            rate = self.exchange_rates[to_curr] / self.exchange_rates[from_curr]
            self.rate_label.config(text=f"1 {from_curr} = {rate:.4f} {to_curr}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def swap_currencies(self):
        """Swap from and to currencies"""
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        self.from_currency.set(to_curr)
        self.to_currency.set(from_curr)
        # Auto-convert after swap
        self.convert_currency()
    
    def refresh_rates(self):
        """Refresh exchange rates from API"""
        if self.fetch_exchange_rates():
            self.update_time_label.config(text=f"Last updated: {self.last_updated}")
            messagebox.showinfo("Success", "Exchange rates updated successfully!")
            self.convert_currency()  # Auto-convert with new rates
        else:
            messagebox.showwarning("Warning", "Using fallback rates!")

def main():
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()