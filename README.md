
# Receipt Analyzer

A Python-based OCR project that extracts text and price information from receipt images.

## Technologies
- Python
- Tesseract OCR
- Pytesseract
- Pillow
- Regular Expressions
- CSV

## Features
- Reads receipt images
- Extracts printed text
- Detects price entries
- Attempts to identify total amount
- Saves extracted text in TXT format
- Exports price data to CSV

## Run
1. Install the required packages.
2. Install Tesseract OCR.
3. Place your receipt image as receipt.jpg.
4. Run:

python receipt_analyzer.py

## Output
- receipt_text.txt
- receipt_analysis.csv
