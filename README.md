# 💳 Subscription Manager (مدير الاشتراكات)

A Python CLI application for managing monthly and yearly subscriptions, tracking spending totals, alerting on upcoming renewals, and saving data automatically.

---

## ✨ Features
* **Add subscriptions:** Record subscription name, price, billing cycle (`monthly` or `yearly`), and next renewal date.
* **View all subscriptions:** Display all saved subscriptions in a clean table.
* **Calculate totals:** Compute total monthly and yearly spending accurately.
* **Upcoming renewals:** Highlight subscriptions renewing soon.
* **Delete subscriptions:** Remove unwanted subscriptions easily.
* **Automatic persistence:** Save and load subscriptions automatically using `subscriptions.json`.

---

## 🏗️ Project Architecture
The project follows a modular structure separating responsibilities across files:

* `main.py`: Main entry point that orchestrates the application flow and connects all modules.
* `storage.py`: Handles loading and saving subscription records in JSON format.
* `logic.py`: Handles cost calculations and upcoming renewal checks.
* `ui.py`: Handles user prompts, input validation, and formatted terminal output.

---

## 🚀 How to Run
1. Make sure **Python 3** is installed on your machine.
2. Open the project folder in VS Code or a terminal.
3. Run the application:
   ```bash
   python main.py
   ## 👩‍💻 Team Members
* **نور تركي الشريف** (`@nourturki`)
* **ندى سالم الشمراني** (`@Ndudinn`)
* **لمار محمد الحربي** (`@lamaralharbie15-lgtm`)