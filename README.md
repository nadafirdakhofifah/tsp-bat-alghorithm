# TSP Bat Algorithm Optimization

Final Project Teknik Optimasi menggunakan Bat Algorithm untuk menyelesaikan Travelling Salesman Problem (TSP) berbasis Streamlit.

---

## 📌 Features

- Upload dataset CSV TSP
- Pilih instance TSP
- Preprocessing otomatis
- Generate distance matrix
- Optimasi rute menggunakan Bat Algorithm
- Menampilkan best route
- Menampilkan total distance
- Visualisasi jalur kota
- Grafik konvergensi

---

## 📂 Dataset

Dataset menggunakan TSPLIB Dataset dari Kaggle:

https://www.kaggle.com/datasets/ziya07/traveling-salesman-problem-tsplib-dataset

Project menggunakan:
- 1 instance TSP
- 10 kota pertama dari instance terpilih

---

## 🛠 Technologies

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- NetworkX

---

## 📁 Project Structure

```bash
tsp-bat-app/
│
├── data/
│   └── tsp_instances_dataset.csv
│
├── src/
│   ├── preprocessing.py
│   ├── bat_algorithm.py
│   └── visualization.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/username/tsp-bat-app.git
```

### 2. Masuk Folder Project

```bash
cd tsp-bat-app
```

### 3. Buat Virtual Environment

```bash
python -m venv env
```

### 4. Aktifkan Environment

Windows:

```bash
env\Scripts\activate
```

Mac/Linux:

```bash
source env/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Aplikasi berjalan di:

```bash
http://localhost:8501
```

---

## 🔄 System Workflow

```text
Upload Dataset
↓
Select TSP Instance
↓
Extract 10 Cities
↓
Generate Distance Matrix
↓
Bat Algorithm Optimization
↓
Fitness Evaluation
↓
Best Route Result
↓
Visualization
```

---

## 📐 Euclidean Distance Formula

```math
d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
```

---

## 📊 Fitness Function

```math
f(\pi)=\sum_{i=1}^{n-1} d_{\pi(i)\pi(i+1)} + d_{\pi(n)\pi(1)}
```

---

## 📷 Output

- Best Route
- Total Distance
- Route Visualization
- Convergence Graph

---

## 👨‍💻 Author

Final Project Teknik Optimasi<br>
Nada Firda Khofifah<br>
Semester 6 — Informatika
