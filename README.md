# 📄 Question Paper Formatter

An all-in-one desktop application designed to streamline the process of creating, formatting, and exporting question papers. Built with Python and SQLite, this tool enables faculty to input questions with metadata like Bloom's Taxonomy Level (BTL), Course Outcome (CO), and marks, and generate a formatted `.docx` question paper with just a few clicks.

---

## 🚀 Features

- 📝 **Add/Edit Questions** with marks, BTL, and CO
- 📂 **Create, Open, Save** question paper files locally
- 📑 **Auto-Formatted Export** to Word `.docx` document
- 🧠 **BTL and CO Mapping** for outcome-based education (OBE)
- 🔎 **Preview Panel** for real-time question layout view
- ⚙️ **Custom Settings** for paper pattern and sections
- 🗃️ **SQLite Database** backend to store and manage question banks

---

## 📸 Screenshots

![Home Screen](assets/home_screen.png)
![Add Question](assets/add_question.png)
![Formatted Output](assets/output.png)

---

## 🛠️ Tech Stack

- **Frontend**: `Tkinter` (Python GUI)
- **Backend**: `SQLite` (Question Database)
- **Export**: `python-docx` (for .docx generation)

---

## 📂 Project Structure

```
Question-paper-formatter/
├── main.py              # Entry point
├── database.py          # SQLite functions
├── export.py            # Word document generation logic
├── gui/                 # UI components and widgets
├── assets/              # Icons and images
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

1. Clone the repo  
```bash
git clone https://github.com/Code-Monish/Question-paper-formatter.git
cd Question-paper-formatter
```

2. Install required packages  
```bash
pip install -r requirements.txt
```

3. Run the application  
```bash
python main.py
```

---

## 📤 Export Output

The exported Word document follows a predefined format, customizable via the settings menu:
- Section-wise formatting (e.g., Part A, B, C)
- Auto-includes marks, BTL levels, and COs
- Neatly aligned, ready-to-print question paper

---



## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Acknowledgements

- Built as part of academic tooling to assist faculty in automating question paper generation.
