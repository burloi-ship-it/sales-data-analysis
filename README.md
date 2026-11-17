# 🛒 Shared Sales Code

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Dependencies](https://img.shields.io/badge/dependencies-none-lightgrey)

A small Python project for displaying and updating product sales stored in a dictionary. It demonstrates reusable, documented functions (docstrings), dictionary manipulation and a simple multi-file project layout suitable for team collaboration with Git.

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [▶️ Usage](#️-usage)
- [🖥️ Sample Output](#️-sample-output)
- [🎯 What I Practiced](#-what-i-practiced)
- [🔮 Possible Improvements](#-possible-improvements)
- [👤 Author](#-author)

---

## ✨ Features

- 📋 **Display sales**: `display_sales()` prints every product with its sold units
- ✏️ **Update sales**: `update_sales()` changes the sales value of a specific product
- 📝 **Documented code**: functions include docstrings describing arguments
- 🗒️ **Product list**: `products.txt` holds a plain-text list of products
- 📦 **Zero dependencies**: runs on the Python standard library only

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python 3.6+ | Core language |
| 🔀 Git / GitHub | Version control and collaboration |

---

## 📁 Project Structure

```text
.
├── shared_sales_code.py   # Display and update sales (main program)
├── hello_world.py         # Minimal "Hello World" script
├── razvan_burloi.py       # Personal greeting script (Git collaboration exercise)
├── products.txt           # List of products
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- 🐍 [Python 3.6+](https://www.python.org/downloads/)
- 🔧 [Git](https://git-scm.com/)

### Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

---

## ▶️ Usage

Run the main program:

```bash
python shared_sales_code.py
```

Use the functions in your own code:

```python
from shared_sales_code import display_sales, update_sales

sales_data = {"Laptop": 50, "Phone": 100, "Television": 30}

update_sales(sales_data, "Phone", 120)
display_sales(sales_data)
```

> ℹ️ Importing the module also runs its demo section. To avoid that, wrap the demo code in `if __name__ == "__main__":`.

---

## 🖥️ Sample Output

```text
Laptop: 50 units.
Phone: 100 units.
Television: 30 units.

Updated sales:
Laptop: 50 units.
Phone: 120 units.
Television: 30 units.
```

---

## 🎯 What I Practiced

- ✅ Writing functions with parameters and Google-style docstrings
- ✅ Iterating over dictionaries with `.items()`
- ✅ Updating dictionary values by key
- ✅ Formatted output with f-strings
- ✅ Organizing and sharing code through Git and GitHub

---

## 🔮 Possible Improvements

- [ ] ➕ Add and remove products
- [ ] 📂 Load products from `products.txt` and persist sales to a file
- [ ] ✅ Validate input (non-negative integers, existing product names)
- [ ] 🧪 Add unit tests with `pytest`
- [ ] 🖥️ Add a CLI with `argparse`

⭐ If you found this project useful, consider giving it a star!
