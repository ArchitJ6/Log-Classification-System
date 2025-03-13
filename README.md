# 🚀 Log Classification System  

This project implements a **hybrid log classification system** using three complementary approaches to handle varying complexity in log patterns. It integrates **Regular Expressions (Regex) ✅, Sentence Transformer + Logistic Regression 🤖, and Large Language Models (LLMs)** 📚 to ensure flexibility and accuracy in classifying log messages.  

## ✨ Features  

- ⚡ **FastAPI Interface**: Provides an API endpoint for classifying log messages from CSV files.  
- 🔍 **Three-Tier Classification**:  
  - **Regex-based classification** ✅ for structured patterns.  
  - **BERT + Logistic Regression** 🤖 for complex, labeled data.  
  - **LLM fallback** 📚 for handling unknown or insufficiently labeled patterns.  
- 📂 **Efficient Model Handling**: Uses a pre-trained model (`log_classifier.joblib`) for inference.  

## 🔄 Classification Flow  

1. 📥 **Log Message Input**  
2. 📝 **Regex Classification**  
   - If a valid class is found, return it.  
   - If the pattern is unknown, proceed to step 3.  
3. 🧠 **BERT-based Classification (if enough training samples exist)**  
   - If confident, return the predicted class.  
   - If uncertain, proceed to step 4.  
4. 🤯 **LLM-based Classification** 📚 
   - Uses a large language model to predict the class for unknown patterns.  

## 🎯 Decision Flow
![decision_flow](decision_flow.png)

## 📂 File Structure  

```
├── models  
│   ├── log_classifier.joblib  
├── testing  
│   ├── test.csv  
│   ├── output.csv  
├── training  
│   ├── dataset  
│   │   ├── data.csv  
│   ├── train.ipynb  
├── bert_helper.py  
├── classify.py  
├── llm_helper.py  
├── main.py  
├── regex_helper.py  
```

## 🌐 API Usage  

### 📌 **Endpoint: `/classify/`**  

- 📤 **Method**: `POST`  
- 📥 **Request**: Upload a CSV file with `source` and `log_message` columns.  
- 📄 **Response**: A classified CSV file with an additional `target_label` column.  

### 📌 **Example Request (Python)**  

```python
import requests

url = "http://localhost:8000/classify/"
files = {"file": open("test.csv", "rb")}

response = requests.post(url, files=files)
if response.status_code == 200:
    with open("classified_output.csv", "wb") as f:
        f.write(response.content)
    print("✅ Classified file saved as classified_output.csv")
else:
    print("❌ Error:", response.json())
```


## ⚙️ Setup & Installation  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/ArchitJ6/Log-Classification-System.git
cd Log-Classification-System
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run FastAPI Server**  
```sh
fastapi run main.py
```

## 🏋️ Model Training  

To train the classification model, run the Jupyter notebook:  

```sh
jupyter notebook training/train.ipynb
```

The model will be saved as `models/log_classifier.joblib`.

## 🧑‍💻 Contributing
Contributions are welcome! Fork the project and submit your pull requests.

## 📜 License
This project is licensed under the **MIT License**.