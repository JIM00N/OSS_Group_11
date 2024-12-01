# **Document Translation System**
202333949 seohee


This project provides an automatic document translation system utilizing Hugging Face's `transformers` library models. It includes functionalities for translation, summarization, and high-frequency word extraction, all integrated with OpenCV for document processing tasks. Built using Python, this system is designed to enhance document workflow efficiency.

-----
### **Project Overview**
**The Document Translation System** enables users to translate texts, summarize long documents, and extract high-frequency words. It leverages pre-trained models from Hugging Face and integrates OpenCV for document handling. The main goal is to simplify the task of processing and translating documents in different languages.


### **Demo or Examples**
Example of translated text from English to Korean using the system.
![Short Demo](https://ifh.cc/g/po3o6J.png)


### **Packages Used**
The following Python packages are used in this project. To install them, please run:
```bash
pip install -r requirements.txt
```
The `requirements.txt` includes:
* `transformers` (version 4.x)
* `opencv-python` (version 4.x)
* `torch` (version 1.x)
* `huggingface_hub` (version 0.10.0)
* `requests` (version 2.25.0)


### **How to Run**
To run the translation system, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/DocTrans.git
cd DocTrans
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Run the translation script:
```bash
python src/main.py
```
The system will ask for text input and the source and target languages.
4. For document translation, you can place a document (PDF, text, etc.) in the `input_documents` folder and execute the respective script.


### **References**
* Hugging Face Transformers Documentation: <https://huggingface.co/docs/transformers>
* OpenCV Documentation: <https://opencv.org/>
* Python Hugging Face Tutorial: <https://huggingface.co/course>
* Various blog posts and tutorials on text translation models, Hugging Face, and OpenCV.

-----
This README provides an overview, setup instructions, and resources for anyone interested in using or contributing to the project.
